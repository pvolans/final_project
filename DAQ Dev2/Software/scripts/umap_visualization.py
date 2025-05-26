import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import umap
from pathlib import Path

def load_all_features(preprocessed_dir):
    """Load and merge all spectral and wavelet features from dataset_preprocessed"""
    print(f"Loading features from: {preprocessed_dir}")
    data = []
    for subdir in Path(preprocessed_dir).glob('*'):
        if subdir.is_dir():
            spectral_files = list((subdir / 'dataset_spectral').glob('*.csv'))
            wavelet_files = list((subdir / 'dataset_wavelets').glob('*.csv'))

            for spec_file, wave_file in zip(spectral_files, wavelet_files):
                try:
                    spec_df = pd.read_csv(spec_file)
                    wave_df = pd.read_csv(wave_file)
                    combined = pd.concat([spec_df, wave_df], axis=1)
                    combined['source'] = subdir.name
                    data.append(combined)
                except Exception as e:
                    print(f"Failed to load {spec_file.name} or {wave_file.name}: {e}")
    if not data:
        raise RuntimeError("No data loaded. Check folder structure and file contents.")
    df = pd.concat(data, ignore_index=True)
    print(f"Loaded {df.shape[0]} rows with {df.shape[1]} columns")
    return df

def visualize_umap(df, label_column='source'):
    labels = df[label_column].values

    # Use only the top 5 high entropy features
    selected_features = [
        'wavelet_detail_1_entropy',
        'wavelet_detail_2_entropy',
        'ar_coeff_1',
        'wavelet_detail_3_entropy',
        'wavelet_detail_6_entropy',
        'ar_coeff_7',
        'ar_coeff_8'


    ]

    features = df[selected_features].copy()

    # Drop rows with NaN or Inf
    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    features.dropna(inplace=True)
    labels = labels[features.index]

    # Scale
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # UMAP
    reducer = umap.UMAP(random_state=42)
    embedding = reducer.fit_transform(features_scaled)

    score = silhouette_score(embedding, labels)
    print(f"Silhouette score = {score:.2f}")

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], hue=labels, palette='tab10')
    plt.title('UMAP Projection of Top Entropy Features')
    plt.xlabel('UMAP-1')
    plt.ylabel('UMAP-2')
    plt.legend(title=label_column, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def main():
    base_dir = Path(__file__).resolve().parent.parent
    preprocessed_dir = base_dir / 'dataset_preprocessed'
    df = load_all_features(preprocessed_dir)
    
    visualize_umap(df)

if __name__ == '__main__':
    main()