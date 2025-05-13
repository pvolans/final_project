import numpy as np
import pandas as pd

# Load CSV
data = pd.read_csv('F:\Final_project/wo_movement_test_data_1_1_L.csv')
signal = data['AMP'].values

# Estimate signal power (assuming the entire dataset represents the signal)
signal_power = np.mean(signal**2)

# Estimate noise power (assumption is that part of the signal is noise)
noise_section = pd.read_csv('F:\Final_project/wo_movement_test_data_1_1.csv')  
noise_signal = noise_section['AMP'].values
noise_power = np.mean(noise_signal**2)

# Calculate SNR
snr = signal_power / noise_power
snr_db = 10*np.log10(snr)
print(f"SNR: {snr_db: .2f} db")