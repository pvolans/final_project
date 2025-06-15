import numpy as np
import pandas as pd
from pathlib import Path
from scipy.signal import welch
from statsmodels.tsa.ar_model import AutoReg
from kymatio import Scattering1D
from umap import UMAP
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import torch
import warnings

# Parameters
fs = 50  # Sampling frequency (Hz)
window_sec = 2.0
window_size = int(fs * window_sec)

# Paths
project_root = Path(__file__).resolve().parent.parent
clean_root = project_root / 'dataset_clean'
preprocessed_root = project_root / 'data_preprocessed'
spectral_root = preprocessed_root / 'data_spectral'
wavelet_root = preprocessed_root / 'data_wavelets'

# Create folders
spectral_root.mkdir(parents=True, exist_ok=True)
wavelet_root.mkdir(parents=True, exist_ok=True)

# Initialize wavelet scattering
J = 6
Q = 8
scattering = Scattering1D(J=J, shape=window_size, Q=Q)

# Function to extract spectral features (AR + Welch)
def extract_spectral_features(window):
    ar_order = 4
    try:
        model = AutoReg(window, lags=ar_order, old_names=False).fit()
        ar_coeffs = model.params.values
    except Exception:
        ar_coeffs = np.zeros(ar_order + 1)

    f, Pxx = welch(window, fs=fs, nperseg=window_size)
    psd = Pxx[:10]  # First 10 bins

    return np.concatenate([ar_coeffs, psd])

# Function to extract wavelet features
def extract_wavelet_features(window):
    with torch.no_grad():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            Sx = scattering(torch.tensor(window, dtype=torch.float32).unsqueeze(0))
        return Sx.mean(dim=-1).squeeze().numpy()

# Function to extract all features from one folder
def process_folder(input_folder, output_spectral, output_wavelet, label):
    files = list(input_folder.glob('*.csv'))
    for file in files:
        df = pd.read_csv(file, index_col='Timestamp')
        amp = df['AMP'].dropna().values
        windows = [amp[i:i+window_size] for i in range(0, len(amp) - window_size + 1, window_size)]

        for i, w in enumerate(windows):
            if len(w) != window_size:
                continue
            # Spectral
            spec_feat = extract_spectral_features(w)
            spec_df = pd.DataFrame([spec_feat])
            spec_df['label'] = label
            spec_df.to_csv(output_spectral / f"{file.stem}_w{i}.csv", index=False)

            # Wavelet
            wave_feat = extract_wavelet_features(w)
            wave_df = pd.DataFrame([wave_feat])
            wave_df['label'] = label
            wave_df.to_csv(output_wavelet / f"{file.stem}_w{i}.csv", index=False)

# Iterate over all subfolders in dataset_clean
for subfolder in clean_root.glob('dataset_*_clean'):
    try:
        sample_label = int(subfolder.name.split('_')[1])  # from dataset_0_clean -> 0
    except ValueError:
        print(f"Skipping folder with unexpected name format: {subfolder.name}")
        continue
    process_folder(subfolder, spectral_root, wavelet_root, sample_label)

# Function to load all features for UMAP
def load_features(folder):
    data = []
    labels = []
    for file in folder.glob('*.csv'):
        df = pd.read_csv(file)
        labels.append(df['label'].iloc[0])
        data.append(df.drop(columns=['label']).values.flatten())
    return np.array(data), np.array(labels)

# Load spectral features
X_spec, y_spec = load_features(spectral_root)
scaler_spec = StandardScaler().fit(X_spec)
X_spec_scaled = scaler_spec.transform(X_spec)

# Load wavelet features
X_wave, y_wave = load_features(wavelet_root)
scaler_wave = StandardScaler().fit(X_wave)
X_wave_scaled = scaler_wave.transform(X_wave)

# Apply UMAP
umap_spec = UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean').fit_transform(X_spec_scaled)
umap_wave = UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean').fit_transform(X_wave_scaled)

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("UMAP - Spectral Features")
plt.scatter(umap_spec[:, 0], umap_spec[:, 1], c=y_spec, cmap='tab10', s=10)
plt.colorbar(label='Label')

plt.subplot(1, 2, 2)
plt.title("UMAP - Wavelet Features")
plt.scatter(umap_wave[:, 0], umap_wave[:, 1], c=y_wave, cmap='tab10', s=10)
plt.colorbar(label='Label')

plt.tight_layout()
plt.savefig(preprocessed_root / 'umap_comparison.png')
plt.show()
