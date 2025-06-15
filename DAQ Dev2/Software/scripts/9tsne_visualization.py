import os
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from pathlib import Path

sns.set(style="whitegrid")

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
                    combined['sample_id'] = subdir.name.split('_')[-1]
                    data.append(combined)
                except Exception as e:
                    print(f"Failed to load {spec_file.name} or {wave_file.name}: {e}")
    if not data:
        raise RuntimeError("No data loaded. Check folder structure and file contents.")
    df = pd.concat(data, ignore_index=True)
    print(f"Loaded {df.shape[0]} rows with {df.shape[1]} columns")
    return df


def visualize_tsne(df, label_column='sample_id'):
    labels = df[label_column].astype(int).values

    # Use only the top the highest entropy features
    selected_features = ['wavelet_approx_mean', 'wavelet_total_energy', 'wavelet_approx_energy', 'wavelet_rel_energy_5', 'wavelet_rel_energy_0', 'wavelet_rel_energy_4', 'wavelet_rel_energy_3', 'wavelet_rel_energy_6', 'wavelet_detail_4_energy', 'wavelet_detail_4_var', 'TEMP', 'wavelet_rel_energy_2', 'wavelet_detail_4_std', 'ar_coeff_2', 'wavelet_detail_5_std', 'wavelet_detail_5_var', 'welch_peak_power', 'wavelet_detail_3_var', 'wavelet_approx_std', 'wavelet_approx_var']


    features = df[selected_features].copy()

    # Drop rows with NaN or Inf
    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    features.dropna(inplace=True)
    labels = labels[features.index]

    # Scale
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # t-SNE
    tsne = TSNE(n_components=3)
    embedding = tsne.fit_transform(features_scaled)

    score = silhouette_score(embedding, labels)
    print(f"Silhouette score (t-SNE) = {score:.2f}")

    # Plot
    fig = px.scatter_3d(
        x=embedding[:, 0], y=embedding[:, 1], z=embedding[:, 2],
        color=labels,
        title="t-SNE 3D Projection of All Features",
        labels={'x': 't-SNE-1', 'y': 't-SNE-2', 'z': 't-SNE-3'}
    )
    fig.update_layout(legend_title_text=label_column)
    fig.update_traces(marker=dict(size=3))  # Smaller dot size

    fig.show()


def main():
    base_dir = Path(__file__).resolve().parent.parent
    preprocessed_dir = base_dir / 'dataset_feature_extracted'
    df = load_all_features(preprocessed_dir)
    visualize_tsne(df)

if __name__ == '__main__':
    main()
