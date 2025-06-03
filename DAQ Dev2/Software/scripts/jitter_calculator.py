import pandas as pd
from pathlib import Path

# Define the dataset root directory relative to this script
dataset_root = Path(__file__).resolve().parent.parent / 'dataset_2'

# Find all CSV files matching the expected pattern recursively
csv_files = list(dataset_root.rglob('data_*.csv'))

print(f"Found {len(csv_files)} dataset files.")

all_intervals = []

# Initialize tracking variables
max_interval = -float('inf')
min_interval = float('inf')
max_file = None
min_file = None
max_interval_value = None
min_interval_value = None

for file in csv_files:
    try:
        df = pd.read_csv(file)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        intervals = df['Timestamp'].diff().dt.total_seconds().dropna()

        # Update global interval list
        all_intervals.extend(intervals.tolist())

        # Check for max and min intervals in this file
        local_max = intervals.max()
        local_min = intervals.min()

        if local_max > max_interval:
            max_interval = local_max
            max_file = file
            max_interval_value = local_max

        if local_min < min_interval:
            min_interval = local_min
            min_file = file
            min_interval_value = local_min

        print(f"Processed {file.name}: {len(intervals)} intervals")

    except Exception as e:
        print(f"Error processing {file.name}: {e}")

# Compute overall jitter metrics
if all_intervals:
    intervals_series = pd.Series(all_intervals) 
    metrics = {
        'mean_interval (s)': intervals_series.mean(),
        'mean_frequency (Hz)': 1 / intervals_series.mean() if intervals_series.mean() != 0 else 0,
        'std_interval (s)': intervals_series.std(),
        'std_frequency (Hz)': 1 / intervals_series.std() if intervals_series.std() != 0 else 0,
        'min_interval (s)': intervals_series.min(),
        'min_frequency (Hz)': 1 / intervals_series.min() if intervals_series.min() != 0 else 0,
        'max_interval (s)':  intervals_series.max(),
        'max_frequency (Hz)': 1 /intervals_series.max() if intervals_series.max() != 0 else 0,
    }


    print("\n=== Overall Jitter Metrics ===")
    print(f"Mean interval: {metrics['mean_interval (s)']:.6f} s ( {metrics['mean_frequency (Hz)']} Hz )")
    print(f"Standard deviation: {pd.Series(all_intervals).std():.6f} s ( {metrics['std_frequency (Hz)']} Hz )")
    print(f"Minimum interval: {min_interval_value:.6f} s ( {metrics['min_frequency (Hz)']} Hz ) in file: {min_file} ")
    print(f"Maximum interval: {max_interval_value:.6f} s ( {metrics['max_frequency (Hz)']} Hz ) in file: {max_file}")
else:
    print("No valid intervals found.")
