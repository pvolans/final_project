import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
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

    # Use only the top 5 high entropy features
    selected_features = [
        'ar_coeff_1','ar_coeff_2','ar_coeff_3','ar_coeff_4','ar_coeff_5',
        'ar_coeff_6','ar_coeff_7','ar_coeff_8','ar_coeff_9','ar_coeff_10',
        'ar_coeff_11','ar_coeff_12','ar_coeff_13','ar_coeff_14','ar_coeff_15',
        'ar_variance','ar_aic','ar_bic','welch_total_power','welch_mean_freq',
        'welch_median_freq','welch_peak_freq','welch_peak_power','welch_spectral_rolloff',
        'welch_spectral_flux','welch_spectral_entropy','welch_delta_power',
        'welch_theta_power','welch_alpha_power','welch_beta_power',
        'wavelet_approx_mean','wavelet_approx_std','wavelet_approx_var',
        'wavelet_approx_energy','wavelet_approx_entropy','wavelet_detail_1_mean',
        'wavelet_detail_1_std','wavelet_detail_1_var','wavelet_detail_1_energy',
        'wavelet_detail_1_entropy','wavelet_detail_2_mean','wavelet_detail_2_std',
        'wavelet_detail_2_var','wavelet_detail_2_energy','wavelet_detail_2_entropy',
        'wavelet_detail_3_mean','wavelet_detail_3_std','wavelet_detail_3_var',
        'wavelet_detail_3_energy','wavelet_detail_3_entropy','wavelet_detail_4_mean',
        'wavelet_detail_4_std','wavelet_detail_4_var','wavelet_detail_4_energy',
        'wavelet_detail_4_entropy','wavelet_detail_5_mean','wavelet_detail_5_std',
        'wavelet_detail_5_var','wavelet_detail_5_energy','wavelet_detail_5_entropy',
        'wavelet_detail_6_mean','wavelet_detail_6_std','wavelet_detail_6_var',
        'wavelet_detail_6_energy','wavelet_detail_6_entropy','wavelet_rel_energy_0',
        'wavelet_rel_energy_1','wavelet_rel_energy_2','wavelet_rel_energy_3',
        'wavelet_rel_energy_4','wavelet_rel_energy_5','wavelet_rel_energy_6',
        'wavelet_total_energy'
    ]

    features = df[selected_features].copy()

    # Drop rows with NaN or Inf
    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    features.dropna(inplace=True)
    labels = labels[features.index]

    # Scale
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # t-SNE
    pca = PCA(n_components=2)
    reduced_features = pca.fit_transform(features_scaled)

    score = silhouette_score(reduced_features, labels)
    print(f"Silhouette score (t-SNE) = {score:.2f}")

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=reduced_features[:, 0], y=reduced_features[:, 1], hue=labels, palette='tab10')
    plt.title('t-SNE Projection of Top Entropy Features')
    plt.xlabel('t-SNE-1')
    plt.ylabel('t-SNE-2')
    plt.legend(title=label_column, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def main():
    base_dir = Path(__file__).resolve().parent.parent
    preprocessed_dir = base_dir / 'dataset_feature_extracted'
    df = load_all_features(preprocessed_dir)
    visualize_tsne(df)

if __name__ == '__main__':
    main()
