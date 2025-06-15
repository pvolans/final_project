import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# --- Config ---
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_ROOT = SCRIPT_DIR.parent / "dataset_feature_extracted"
SPECTRAL_FOLDER = "dataset_spectral"
WAVELET_FOLDER = "dataset_wavelets"
ODD_POINTS = list(range(1, 20, 2))

# --- Step 1: Load dataset ---
X = []
y = []

selected_features = ['wavelet_approx_mean', 'wavelet_total_energy', 'wavelet_approx_energy', 'wavelet_rel_energy_5', 'wavelet_rel_energy_0', 'wavelet_rel_energy_4', 'wavelet_rel_energy_3', 'wavelet_rel_energy_6', 'wavelet_detail_4_energy', 'wavelet_detail_4_var', 'TEMP', 'wavelet_rel_energy_2', 'wavelet_detail_4_std', 'ar_coeff_2', 'wavelet_detail_5_std', 'wavelet_detail_5_var', 'welch_peak_power', 'wavelet_detail_3_var', 'wavelet_approx_std', 'wavelet_approx_var']

for sample_folder in sorted(DATA_ROOT.glob("dataset_sample_*")):
    label = int(sample_folder.name.split("_")[-1])
    for point in ODD_POINTS:
        spectral_files = sorted((sample_folder / SPECTRAL_FOLDER).glob(f"data_*_{point}_*_spectral.csv"))
        wavelet_files = sorted((sample_folder / WAVELET_FOLDER).glob(f"data_*_{point}_*_wavelets.csv"))

        for spec_file, wav_file in zip(spectral_files, wavelet_files):
            try:
                df_spec = pd.read_csv(spec_file)
                df_wav = pd.read_csv(wav_file)
                sample = pd.concat([df_spec, df_wav], axis=1)
                selected_df = sample[selected_features]

                X.append(selected_df.values.flatten())
                y.append(label)
            except Exception as e:
                print(f"Skipping {spec_file}, {wav_file} due to error: {e}")

X = np.array(X)
y = np.array(y)

# --- Step 2: Normalize Features ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Step 3: Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, stratify=y, random_state=42)

# --- Step 4: Reshape for 1D CNN ---
n_features = X_train.shape[1]
X_train = X_train.reshape((-1, n_features, 1))
X_test = X_test.reshape((-1, n_features, 1))

# --- Step 5: Build 1D CNN Model ---
model = models.Sequential([
    layers.Input(shape=(n_features, 1)),
    layers.Conv1D(64, kernel_size=5, activation='sigmoid'),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(128, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(64, kernel_size=3, activation='sigmoid'),
    layers.GlobalAveragePooling1D(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.4),
    layers.Dense(len(np.unique(y)), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# --- Step 6: Train Model ---
history = model.fit(X_train, y_train,
                    validation_split=0.1,
                    epochs=200,
                    batch_size=16,
                    verbose=1)

# --- Step 7: Evaluate ---
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy:.4f}")

# --- Step 8: Plot Accuracy and Loss ---
plt.figure(figsize=(12, 5))

# Accuracy plot
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy')
plt.legend()
plt.grid(True)

# Loss plot
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Model Loss')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Step 9: Confusion Matrix ---
# Predict classes
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

print("Classification Report:")
print(classification_report(y_test, y_pred))


# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y))

specificity_list = []
for i in range(len(cm)):
    TP = cm[i, i]
    FN = cm[i, :].sum() - TP
    FP = cm[:, i].sum() - TP
    TN = cm.sum() - (TP + FP + FN)
    specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
    specificity_list.append(specificity)

# Print specificities
for i, spec in enumerate(specificity_list):
    print(f"Specificity (class {i}): {spec:.4f}")

# Plot confusion matrix
fig, ax = plt.subplots(figsize=(8, 6))
disp.plot(ax=ax, cmap='Blues', xticks_rotation=45)
plt.title("Confusion Matrix")
plt.grid(False)
plt.tight_layout()
plt.show()