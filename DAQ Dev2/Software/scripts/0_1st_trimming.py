import pandas as pd
from pathlib import Path

# Function to load interpolated CSVs
def load_uniform(file_path):
    df = pd.read_csv(file_path)
    return df

def trim_signal_symmetric(data, target_length):
    current_length = len(data)
    if current_length < target_length:
        raise ValueError(f"Signal length {current_length} is less than target {target_length}")
    excess = current_length - target_length
    start_trim = excess // 2
    end_trim = excess - start_trim
    return data.iloc[start_trim:current_length-end_trim].reset_index(drop=True)

# Define project directories
script_dir   = Path(__file__).resolve().parent
project_root = script_dir.parent
dataset_root = project_root / 'dataset_2_40'
pre_processed   = project_root / 'dataset_1st_trim'
pre_processed.mkdir(exist_ok=True)

# -------------------- #
# Collect statistics
# -------------------- #
all_lengths = []
file_count = 0
COLUMNS = ['Timestamp', 'DIST', 'AMP', 'TEMP', 'VOLT', 'Angle', 'ON', 'Movement']

for sub in dataset_root.iterdir():
    if not sub.is_dir():
        continue

    for f in sub.glob('data_*.csv'):
        try:
            df = load_uniform(f)
            length = len(df)
            all_lengths.append(length)
            file_count += 1
        except Exception as e:
            print(f"Error reading {f.name}: {e}")

if all_lengths:
    print("\n--- Dataset Summary ---")
    print(f"Total files: {file_count}")
    print(f"Shortest signal length: {min(all_lengths)}")
    print(f"Longest signal length: {max(all_lengths)}")
    print("------------------------\n")
else:
    print("No valid signals found.")
    exit()

# Prompt user for desired sample length
time_series_sample = int(input("Enter desired uniform signal length for trimming: "))

# -------------------- #
# Begin signal processing
# -------------------- #
for sub in dataset_root.iterdir():
    if not sub.is_dir():
        continue

    out_sub = pre_processed / f"{sub.name}_trimmed"
    out_sub.mkdir(parents=True, exist_ok=True)

    # Build lookup by sample and point number
    files = list(sub.glob('data_*.csv'))
    lookup = {}
    for f in files:
        parts = f.stem.split('_')
        if len(parts) != 3:
            print(f"Skipping unexpected filename format: {f.name}")
            continue
        _, sample, point = parts
        lookup[(int(sample), int(point))] = f
        sig      = load_uniform(f)

        if len(sig) < time_series_sample:
            print(f"Too short: {f.name}")
            continue

        print(f"Processing sample {sample}, point {point}")

        if 'AMP' not in sig.columns or 'AMP' not in sig.columns:
            print(f"AMP column missing in files; skipping {f.name}")
            continue

        
        trimmed = trim_signal_symmetric(sig, time_series_sample)

        out_path = out_sub / f"{f.name}"
        trimmed.to_csv(out_path, index=False, header=True)
        print(f"Saved to {out_path}")
exec(open('1noise_canceling.py').read())