import pandas as pd
from pathlib import Path

# Get script and project roots
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

# Define source and target dataset roots
dataset_root = project_root / 'dataset'
interpolated_root = project_root / 'dataset_interpolated'

# Create the top-level interpolated folder if it doesn't exist
interpolated_root.mkdir(exist_ok=True)

# Define your resampling rate (e.g., ~57 Hz)
target_rate = '20ms'

# Process each subfolder under 'dataset/'
for sub in dataset_root.iterdir():
    if sub.is_dir() and sub.name.startswith('dataset_'):
        # Create a parallel output subfolder
        out_sub = interpolated_root / f"{sub.name}_interpolated"
        out_sub.mkdir(parents=True, exist_ok=True)

        # Find all CSV files inside this dataset folder
        for csv_file in sub.rglob('data_*.csv'):
            try:
                # Load and index by timestamp
                df = pd.read_csv(csv_file, parse_dates=['Timestamp'])
                df = df.set_index('Timestamp').sort_index()

                # Resample and interpolate
                df_resampled = df.resample(target_rate).mean()
                df_interp = df_resampled.interpolate(method='time')

                # Save interpolated data to the new folder (same filename)
                out_path = out_sub / csv_file.name
                df_interp.to_csv(out_path, index=True)

                print(f"Saved interpolated: {out_path}")
            except Exception as e:
                print(f"Error processing {csv_file}: {e}")

print("Interpolation complete.")
