import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import numpy as np

def process_file(filename):
    df = pd.read_csv(filename)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    time = (df['Timestamp'] - df['Timestamp'].iloc[0]).dt.total_seconds().values
    time_diffs = np.diff(time)
    sample_rate = 1 / np.mean(time_diffs)
    amp = df['AMP'].values
    return time, amp, sample_rate

# Process both files
time1_wm, amp1_wm, sr1_wm = process_file("movement_test_data_1_1_L.csv")  # Sample 1: with movement
time1_wom, amp1_wom, sr1_wom = process_file("wo_movement_test_data_1_1_L.csv")  # Sample 1: without movement

time2_wm, amp2_wm, sr2_wm = process_file("movement_test_data_4_1_L.csv")  # Sample 1: with movement
time2_wom, amp2_wom, sr2_wom = process_file("wo_movement_test_data_4_0_L.csv")  # Sample 1: without movement

"""
# Plot time series side by side
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(time1, amp1, label='Sample 1 (No Movement)')
plt.title("Amplitude Time Series - No Movement")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(time2, amp2, label='Sample 2 (With Movement)', color='orange')
plt.title("Amplitude Time Series - With Movement")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
"""
# Plot spectrograms side by side
f1_wm, t1_spec_wm, Sxx1_wm = spectrogram(amp1_wm, fs=sr1_wm, nperseg=256)
f1_wom, t1_spec_wom, Sxx1_wom = spectrogram(amp1_wom, fs=sr1_wom, nperseg=256)
f2_wm, t2_spec_wm, Sxx2_wm = spectrogram(amp2_wm, fs=sr2_wm, nperseg=256)
f2_wom, t2_spec_wom, Sxx2_wom = spectrogram(amp2_wom, fs=sr2_wom, nperseg=256)

plt.figure(figsize=(14, 6))

plt.subplot(2, 2, 1)
plt.pcolormesh(t1_spec_wm, f1_wm, 10 * np.log10(Sxx1_wm), shading='gouraud')
plt.title('Spectrogram for Sample 1 - With Movement')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(label='Power [dB]')

plt.subplot(2, 2, 2)
plt.pcolormesh(t1_spec_wom, f1_wom, 10 * np.log10(Sxx1_wom), shading='gouraud')
plt.title('Spectrogram for Sample 1 - Without Movement')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(label='Power [dB]')

plt.subplot(2, 2, 3)
plt.pcolormesh(t2_spec_wm, f2_wm, 10 * np.log10(Sxx2_wm), shading='gouraud')
plt.title('Spectrogram for Sample 2 - With Movement')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(label='Power [dB]')

plt.subplot(2, 2, 4)
plt.pcolormesh(t2_spec_wom, f2_wom, 10 * np.log10(Sxx2_wom), shading='gouraud')
plt.title('Spectrogram for Sample 2 - Without Movement')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.colorbar(label='Power [dB]')

plt.tight_layout()
plt.show()
