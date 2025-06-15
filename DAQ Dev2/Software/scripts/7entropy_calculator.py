import pandas as pd
import numpy as np
from scipy.stats import entropy
from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set(style="whitegrid")

def calculate_entropy(df, n_bins=10):
    entropies = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        values = df[col].dropna()
        if values.nunique() < 2:
            entropies[col] = 0
            continue
        hist, _ = np.histogram(values, bins=n_bins, density=True)
        hist = hist + 1e-12  # Avoid log(0)
        prob = hist / np.sum(hist)
        entropies[col] = entropy(prob, base=2) / np.log2(n_bins)
    return pd.Series(entropies)

def calculate_mutual_info(X, y):
    X_filled = X.fillna(0)
    mi_scores = mutual_info_classif(X_filled, y, discrete_features=False)
    return pd.Series(mi_scores, index=X.columns)

def load_combined_data(root_dir):
    combined = []
    for i in range(25):  # sample_0 to sample_4
        for feat_type in ['dataset_spectral', 'dataset_wavelets']:
            folder = Path(root_dir) / f"dataset_sample_{i}" / feat_type
            if not folder.exists():
                continue
            files = list(folder.glob("*.csv"))
            for f in files:
                df = pd.read_csv(f)
                df['sample_id'] = i
                df['source'] = feat_type
                combined.append(df)
    return pd.concat(combined, ignore_index=True)

def main():
    root_dir = "F:/Final_project/DAQ Dev2/Software/dataset_feature_extracted"
    df = load_combined_data(root_dir)
    print(f"Loaded {df.shape[0]} rows with {df.shape[1]} columns")

    # Prepare features and labels
    y = df['sample_id']
    X = df.drop(columns=['sample_id', 'source'], errors='ignore')
    X = X.select_dtypes(include=[np.number])  # Only numeric

    # Calculate entropy
    entropies = calculate_entropy(X)
    print("Top 5 features by entropy:")
    print(entropies.sort_values(ascending=False).head(25))

    # Calculate mutual information
    mi_scores = calculate_mutual_info(X, y)
    print("Top 5 features by mutual information:")
    print(mi_scores.sort_values(ascending=False).head(25))

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    entropies.sort_values(ascending=False).head(10).plot(kind='barh', ax=axes[0], color='skyblue')
    axes[0].set_title("Top 10 Features by Entropy")
    axes[0].invert_yaxis()

    mi_scores.sort_values(ascending=False).head(10).plot(kind='barh', ax=axes[1], color='orange')
    axes[1].set_title("Top 10 Features by Mutual Information")
    axes[1].invert_yaxis()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
