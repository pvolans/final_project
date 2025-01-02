import os
import pandas as pd
import numpy as np
from scipy.signal import welch
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Function to compute Welch's method features
def compute_psd_features(df_L, sampling_rate):
    amp_series = df_L['AMP']
    freqs, psd = welch(amp_series, fs=sampling_rate)
    return psd

# Prepare dataset
samples = 9
data_series_per_sample = 36
sampling_rate = 57.74
features = []
labels = []

script_dir = os.path.dirname(os.path.abspath(__file__))

# Loop over all samples and data series
for sample_id in [3,8]:
    for series_id in range(data_series_per_sample):
        csv_file_L = os.path.join(script_dir, f"data_{sample_id}_{series_id}_L.csv")  # Adjust filenames
        csv_file = os.path.join(script_dir, f"data_{sample_id}_{series_id}.csv")  # Adjust filenames

        try:
            # Load the data
            df_L = pd.read_csv(csv_file_L)
            df = pd.read_csv(csv_file)
            df_L['Timestamp'] = pd.to_datetime(df_L['Timestamp'])
            
            # Calculate sampling rate dynamically if needed
            time_diffs = df_L['Timestamp'].diff().dt.total_seconds().dropna()
            avg_sampling_rate = 1 / time_diffs.mean() if not time_diffs.empty else sampling_rate
            print(f"avg_sampling rate: {avg_sampling_rate}")

            amp_series = df_L['AMP'] - df['AMP'] 

            # Compute Welch's features
            freqs, psd = welch(amp_series, fs=avg_sampling_rate)
            
            # Append features and label
            features.append(psd)
            labels.append(sample_id)
        except Exception as e:
            print(f"Error processing {csv_file_L}: {e}")

# Convert to NumPy arrays
features = np.array(features)
labels = np.array(labels)

# Normalize features
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Reshape data for LSTM (samples, timesteps, features)
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Build LSTM model
model = Sequential([
    LSTM(64, input_shape=(X_train.shape[1], 1), return_sequences=False),
    Dense(32, activation='relu'),
    Dense(samples, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_split=0.3, epochs=50, batch_size=16, verbose=2)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Generate predictions
y_pred = np.argmax(model.predict(X_test), axis=1)

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)
cmd = ConfusionMatrixDisplay(confusion_matrix=cm)
cmd.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

