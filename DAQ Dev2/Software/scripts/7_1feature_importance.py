from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from collections import Counter

# --- Config ---
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_ROOT = SCRIPT_DIR.parent / "dataset_feature_extracted"
SPECTRAL_FOLDER = "dataset_spectral"
WAVELET_FOLDER = "dataset_wavelets"
ODD_POINTS = list(range(1, 20, 2))

# --- Step 1: Load dataset ---
X = []
y = []
feature_names = None  # to hold column names

for sample_folder in sorted(DATA_ROOT.glob("dataset_sample_*")):
    label = int(sample_folder.name.split("_")[-1])  # class label from folder name
    for point in ODD_POINTS:
        spectral_files = sorted((sample_folder / SPECTRAL_FOLDER).glob(f"data_*_{point}_*_spectral.csv"))
        wavelet_files = sorted((sample_folder / WAVELET_FOLDER).glob(f"data_*_{point}_*_wavelets.csv"))

        for spec_file, wav_file in zip(spectral_files, wavelet_files):
            try:
                df_spec = pd.read_csv(spec_file)
                df_wav = pd.read_csv(wav_file)
                sample = pd.concat([df_spec, df_wav], axis=1)
                if feature_names is None:
                    feature_names = sample.columns.tolist()
                X.append(sample.values.flatten())
                y.append(label)
            except Exception as e:
                print(f"Skipping {spec_file}, {wav_file} due to error: {e}")

X = np.array(X)
y = np.array(y)

# --- Step 2: Fit Random Forest and get top 10 features ---
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X, y)
importances = rf.feature_importances_

FEATURE_NUM = 26
# Top feature indices and names
top_indices = np.argsort(importances)[::-1][:FEATURE_NUM]
top_feature_names = [feature_names[i] for i in top_indices]
feature_counts = Counter(top_feature_names)
duplicate_features = {feat: count for feat, count in feature_counts.items() if count > 1}

if duplicate_features:
    print("Duplicate features found:")
    for feat, count in duplicate_features.items():
        print(f"{feat}: {count} times")
        top_feature_names.remove(feat)

else:
    print("No duplicate features among top selected.")

print(f"Top {FEATURE_NUM} features (by name):", top_feature_names)


# --- Step 4: Cross-validate SVM with top 10 features ---
X_top = X[:, top_indices]
svm = SVC(kernel='rbf', gamma='scale')
scores = cross_val_score(svm, X_top, y, cv=5)

print(f"SVM accuracy with top {FEATURE_NUM} features:", scores.mean())
