import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import f_classif
from umap import UMAP
import matplotlib.pyplot as plt
from datetime import datetime

# === Paths ===
project_root = Path(__file__).resolve().parent.parent
pre_dir = project_root / 'dataset_preprocessed'
spectral_dir = pre_dir / 'dataset_spectral'
wavelet_dir = pre_dir / 'dataset_wavelets'
output_png = pre_dir / 'umap_top_features.png'

# === Load data ===
def load_features(folder: Path):
    data, labels, sample_ids, feature_names = [], [], [], []
    files = sorted(folder.glob('*.csv'))
    if not files:
        raise FileNotFoundError(f"No CSVs found in {folder}")

    for f in files:
        df = pd.read_csv(f)

        # Extract sample ID from filename (e.g., clean_data_0_11_wavelets.csv)
        parts = f.stem.split('_')
        sample_id = int(parts[2]) if len(parts) > 2 else 0
        sample_ids.append(sample_id)

        # Use 'Movement' column as a label
        lbl = df['Movement'].iloc[0] if 'Movement' in df.columns else 0
        labels.append(lbl)

        # Drop non-feature columns
        df = df.drop(columns=['Timestamp', 'ON', 'Movement'], errors='ignore')

        # Keep only numeric values
        df_num = df.apply(pd.to_numeric, errors='coerce').dropna(axis=1)

        # Store feature names once
        if not feature_names:
            feature_names = df_num.columns.tolist()

        # Flatten and store
        data.append(df_num.values.flatten())

    min_len = min(len(row) for row in data)
    X = np.vstack([row[:min_len] for row in data])
    return X, np.array(labels), np.array(sample_ids), feature_names[:min_len]

# Load spectral and wavelet data
X_spec, y_spec, sample_ids_spec, spec_names = load_features(spectral_dir)
X_wave, y_wave, sample_ids_wave, wave_names = load_features(wavelet_dir)

# Combine features and sample IDs
X_combined = np.concatenate([X_spec, X_wave], axis=1)
combined_names = spec_names + wave_names
sample_ids = sample_ids_spec  # Assumes alignment is valid

# Standardize features
scaler = StandardScaler().fit(X_combined)
X_scaled = scaler.transform(X_combined)

# Feature ranking using ANOVA F-score
f_scores, _ = f_classif(X_scaled, sample_ids)
ranked = sorted(zip(f_scores, combined_names), reverse=True)
top_features = [name for _, name in ranked[:5]]

print("Top 5 discriminative features:")
for score, name in ranked[:5]:
    print(f"  {name:30s} F-score = {score:.2f}")

# Select top features for UMAP
sel_idx = [combined_names.index(name) for name in top_features]
X_selected = X_scaled[:, sel_idx]

# UMAP projection
umap_result = UMAP(n_neighbors=15, min_dist=0.1, metric='euclidean',random_state=42, init='spectral' ).fit_transform(X_selected)

# Plotting
plt.figure(figsize=(8, 6))
sc = plt.scatter(umap_result[:, 0], umap_result[:, 1], c=sample_ids, cmap='tab10', s=30)
plt.title("UMAP on Top 5 Discriminative Features")
plt.colorbar(sc, label='Sample ID')
plt.tight_layout()
plt.savefig(output_png, dpi=150)
print(f"UMAP plot saved to {output_png}")
plt.show()

X_spec_scaled = StandardScaler().fit_transform(X_spec)
f_spec, _   = f_classif(X_spec_scaled, sample_ids_spec)
spec_ranked = sorted(zip(f_spec, spec_names), reverse=True)
print("\nTop spectral features by F-score:")
for score, name in spec_ranked[:5]:
    print(f"  {name:25s}  F-score = {score:.2f}")