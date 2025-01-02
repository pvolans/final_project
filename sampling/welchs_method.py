import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
import numpy as np

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a folder to save graphs if it doesn't exist
graph_folder = os.path.join(script_dir, "Graph")
os.makedirs(graph_folder, exist_ok=True)

# File range and initialization
min_idx_file = 1
max_idx_file = 7

# Prepare lists of files
csv_files_L = [os.path.join(script_dir, f"data_8_{y}_L.csv") for y in range(min_idx_file, max_idx_file)]
csv_files = [os.path.join(script_dir, f"data_8_{y}.csv") for y in range(min_idx_file, max_idx_file)]

# Loop through files
for i in range(min_idx_file, max_idx_file):
    try:
        # Load corresponding files
        df_L = pd.read_csv(csv_files_L[i - min_idx_file])
        df = pd.read_csv(csv_files[i - min_idx_file])

        # Ensure Timestamp is parsed correctly
        df_L['Timestamp'] = pd.to_datetime(df_L['Timestamp'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Calculate average sampling rate
        time_diffs = df_L['Timestamp'].diff().dt.total_seconds().dropna()
        avg_sampling_rate = 1 / time_diffs.mean() if not time_diffs.empty else 56.0  # Fallback sampling rate
        print(f"Avg sampling rate for {csv_files_L[i - min_idx_file]}: {avg_sampling_rate:.2f} Hz")

        # Extract AMP signal difference
        amp_series = df_L['AMP'] - df['AMP']

        # Apply Welch's method
        freqs, psd = welch(
            amp_series,
            fs=avg_sampling_rate,
            nperseg=512,          # Segment length
            noverlap=256,         # 50% overlap
            nfft=512,             # FFT length
            scaling='density',    # Power density scaling
            window='hann'         # Hann window
        )

        # Plot Welch's Method results
        plt.figure()
        plt.semilogy(freqs, psd)
        plt.xlim([0, 30])  # Frequency limit
        plt.grid(which='both', linestyle='--', linewidth=0.5)  # MATLAB-style grid
        plt.xlabel('Frequency (Hz)', fontsize=12)
        plt.ylabel('Power Spectral Density', fontsize=12)

        # Title and Filename
        base_filename = os.path.basename(csv_files_L[i - min_idx_file]).split('.')[0]
        plt.title(f"Welch's Method - {base_filename}\n(Sampling Rate: {avg_sampling_rate:.2f} Hz)")

        # Save the plot
        graph_path = os.path.join(graph_folder, f"welch_{base_filename}_py.png")
        plt.savefig(graph_path, dpi=300)  # High-resolution output
        plt.close()
        print(f"Graph saved for {base_filename}: {graph_path}")

    except Exception as e:
        print(f"Error processing file {csv_files_L[i - min_idx_file]}: {e}")
