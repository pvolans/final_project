import pandas as pd
from pathlib import Path

time_series_sample = 3900

# Function to load interpolated CSVs
def load_uniform(file_path):
    df = pd.read_csv(
        file_path
    )
    return df

def validate_signal_length(data, min_length=time_series_sample):
    return len(data) >= min_length

def trim_signal_symmetric(data, target_length=time_series_sample):
    current_length = len(data)
    if current_length < target_length:
        raise ValueError(f"Signal length {current_length} is less than target {target_length}")
    excess = current_length - target_length
    start_trim = excess // 2
    end_trim = excess - start_trim
    return data.iloc[start_trim:current_length-end_trim].reset_index(drop=True)

# Define project directories
script_dir        = Path(__file__).resolve().parent
project_root      = script_dir.parent
dataset_root      = project_root / 'dataset_2'
clean_root        = project_root / 'dataset_clean'
clean_root.mkdir(exist_ok=True)

# Process each dataset subfolder
for sub in dataset_root.iterdir():
    if not sub.is_dir():
        continue

    out_sub = clean_root / f"{sub.name}_clean"
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

    # Iterate signal runs (odd point numbers)
    for (sample, point), on_file in sorted(lookup.items()):
        if point % 2 != 1:
            continue
        off_key = (sample, point + 1)
        if off_key not in lookup:
            print(f"Missing OFF file for {on_file.name}")
            continue

        off_file = lookup[off_key]
        sig      = load_uniform(on_file)
        noise    = load_uniform(off_file)

        if not validate_signal_length(data=sig, min_length=time_series_sample):
            print(f"Too short: {on_file.name}")
            continue

        if not validate_signal_length(data=noise, min_length=time_series_sample):
            print(f"Too short: {off_file.name}")
            continue

        # Debug: inspect columns and ranges
        print(f"Processing sample {sample}, point {point}")
        print(f"ON range: {sig.index.min()} to {sig.index.max()}")
        print(f"OFF range: {noise.index.min()} to {noise.index.max()}")

        if 'AMP' not in sig.columns or 'AMP' not in noise.columns:
            print(f"AMP column missing in files; skipping {on_file.name}")
            continue

        # Align noise AMP to signal's timestamp grid, filling missing with 0
        noise_amp_aligned = noise['AMP'].reindex(sig.index).fillna(0)

        # Subtract only the 'AMP' channel
        clean = sig.copy()
        clean['AMP'] = sig['AMP'] - noise_amp_aligned

        # Save cleaned CSV including all other columns
        out_path = out_sub / f"clean_{on_file.name}"
        clean = trim_signal_symmetric(clean)
        clean.to_csv(out_path, index=False, header=False)
        print(f"Saved cleaned AMP to {out_path}")

print("Noise removal (AMP only) complete.")
