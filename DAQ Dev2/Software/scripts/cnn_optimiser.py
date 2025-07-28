import numpy as np
import pandas as pd

import itertools
import gc

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, accuracy_score

from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import backend as K

import matplotlib.pyplot as plt

from pathlib import Path
import csv


# --- Config ---
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_ROOT = SCRIPT_DIR.parent / "dataset_feature_extracted"
SPECTRAL_FOLDER = "dataset_spectral"
WAVELET_FOLDER = "dataset_wavelets"
ODD_POINTS = list(range(1, 20, 2))
RESULTS_CSV = SCRIPT_DIR / "best_configs_log.csv"
# --- Step 1: Load dataset ---
X = []
y = []

selected_features = ['wavelet_approx_mean', 'wavelet_total_energy', 'wavelet_approx_energy', 'wavelet_rel_energy_5', 'wavelet_rel_energy_0', 'wavelet_rel_energy_4', 'wavelet_rel_energy_3', 'wavelet_rel_energy_6', 'wavelet_detail_4_energy', 'wavelet_detail_4_var', 'TEMP', 'wavelet_rel_energy_2', 'wavelet_detail_4_std', 'ar_coeff_2', 'wavelet_detail_5_std', 'wavelet_detail_5_var', 'welch_peak_power', 'wavelet_detail_3_var', 'wavelet_approx_std', 'wavelet_approx_var', 'wavelet_detail_5_energy', 'welch_total_power', 'wavelet_detail_3_energy', 'welch_delta_power', 'wavelet_detail_6_std']

# Initialize CSV file with headers
with open(RESULTS_CSV, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
        'iteration', 'accuracy',
        'activation_1', 'activation_2', 'activation_3',
        'kernel_size_1', 'kernel_size_2',
        'filters_conv1', 'filters_conv2',
        'dropout_rate'
    ])
    writer.writeheader()


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

# --- Step 5: Define Search Space ---
activation_options = ['relu', 'sigmoid', 'tanh']
kernel_sizes = [5, 7, 9]
conv_filters = [64, 128, 256, 512]
dropout_rates = [0.4, 0.5]
epochs = 100
batch_size = 16

# Store best result
best_config = None
best_accuracy = 0.0

# --- Automated Grid Search ---
all_configs = list(itertools.product(
    activation_options, activation_options,  # act2, act3
    kernel_sizes, kernel_sizes,              # k1, k2
    conv_filters, conv_filters,              # f1, f2
    dropout_rates                            # dropout_rate
))
total_iterations = len(all_configs)
current_iteration = 0

for act2, act3, k1, k2, f1, f2, dropout_rate in all_configs:
    current_iteration += 1
    config = {
        'activation_1': 'relu',
        'activation_2': act2,
        'activation_3': act3,
        'kernel_size_1': k1,
        'kernel_size_2': k2,
        'filters_conv1': f1,
        'filters_conv2': f2,
        'dropout_rate': dropout_rate
    }
    print(f"[{current_iteration}/{total_iterations}] Testing config: {config}")
    try:
        # Build model
        model = models.Sequential([
            layers.Input(shape=(X_train.shape[1], 1)),
            layers.Conv1D(f1, kernel_size=k1, activation='relu', padding='same'),
            layers.MaxPooling1D(pool_size=2),
            layers.Conv1D(f2, kernel_size=k2, activation=act2, padding='same'),
            layers.MaxPooling1D(pool_size=2),
            layers.Conv1D(64, kernel_size=3, activation=act3, padding='same'),
            layers.GlobalAveragePooling1D(),
            layers.Dense(64, activation='relu'),
            layers.Dropout(dropout_rate),
            layers.Dense(len(np.unique(y)), activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        # Early stopping
        es = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=0)

        # Fit model
        model.fit(
            X_train, y_train,
            validation_split=0.1,
            epochs=epochs,
            batch_size=batch_size,
            verbose=0,
            callbacks=[es]
        )

        # Evaluate
        y_pred = np.argmax(model.predict(X_test, verbose=0), axis=1)
        acc = accuracy_score(y_test, y_pred)

        if acc > best_accuracy:
            best_accuracy = acc
            best_config = config.copy()
            print(f"New best accuracy: {best_accuracy:.4f} with config: {best_config}")

            # Save the new best config to CSV
            with open(RESULTS_CSV, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[
                    'iteration', 'accuracy',
                    'activation_1', 'activation_2', 'activation_3',
                    'kernel_size_1', 'kernel_size_2',
                    'filters_conv1', 'filters_conv2',
                    'dropout_rate'
                ])
                writer.writerow({
                    'iteration': current_iteration,
                    'accuracy': best_accuracy,
                    **best_config
                })
        # Clear memory
        del model
        K.clear_session()
        gc.collect()

    except Exception as e:
        print(f"Skipped config {config} due to: {e}")

print("\nBest config found:")
print(best_config)
print(f"Best Accuracy: {best_accuracy:.4f}")
