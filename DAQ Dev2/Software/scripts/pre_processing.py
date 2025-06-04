import pandas as pd
from pathlib import Path

time_series_length = 3900

# Load raw CSV without modifying column headers
def load_raw(file_path):
    df = pd.read_csv(file_path, header=0)
    return df

def validate_signal_length(data, min_length=time_series_length):
    return len(data) >= min_length

def trim_signal_symmetric(data, target_length=time_series_length):
    current_length = len(data)
    if current_length < target_length:
        raise ValueError(f"Signal length {current_length} is less than target {target_length}")
    excess = current_length - target_length
    start_trim = excess // 2
    end_trim = excess - start_trim
    return data.iloc[start_trim:current_length-end_trim].reset_index(drop=True)

# Set paths
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
raw_root = project_root / 'dataset_2'
clean_root = project_root / 'dataset_preprocessed'
clean_root.mkdir(exist_ok=True)

# Process each sample folder
for sub in raw_root.iterdir():
    if not sub.is_dir():
        continue

    out_sub = clean_root / f"{sub.name}"
    out_sub.mkdir(parents=True, exist_ok=True)

    files = list(sub.glob('data_*.csv'))
    lookup = {}
    for f in files:
        parts = f.stem.split('_')
        if len(parts) != 3:
            print(f"Skipping unexpected filename format: {f.name}")
            continue
        _, sample, point = parts
        lookup[(int(sample), int(point))] = f

    for (sample, point), sig_file in sorted(lookup.items()):
        if point % 2 != 1:
            continue

        noise_key = (sample, point + 1)
        if noise_key not in lookup:
            print(f"Missing noise file for {sig_file.name}")
            continue

        noise_file = lookup[noise_key]
        sig = load_raw(sig_file)
        noise = load_raw(noise_file)

        if not validate_signal_length(sig, min_length=time_series_length):
            print(f"Too short: {sig_file.name}")
            continue
        if not validate_signal_length(noise, min_length=time_series_length):
            print(f"Too short: {noise_file.name}")
            continue

        if sig.shape[1] < 1 or noise.shape[1] < 1:
            print(f"Empty file or bad format: {sig_file.name}")
            continue

        # Subtract only first column (assumed AMP)
        sig_cleaned = sig.copy()
        sig_cleaned.iloc[:, 1] = sig.iloc[:, 1].values - noise.iloc[:, 1].reindex(sig.index).fillna(1).values

        try:
            trimmed = trim_signal_symmetric(sig_cleaned)
        except ValueError as e:
            print(e)
            continue

        # Save with all columns and header intact
        out_path = out_sub / f"{sig_file.name}"
        trimmed.to_csv(out_path, index=False)
        print(f"Saved cleaned: {out_path}")

print("Signal cleaning complete.")