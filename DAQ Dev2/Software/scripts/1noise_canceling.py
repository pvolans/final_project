import pandas as pd
from pathlib import Path

# Function to load interpolated CSVs
def load_uniform(file_path):
    df = pd.read_csv(
        file_path,
        parse_dates=['Timestamp'],
        index_col='Timestamp'
    )
    df = df[~df.index.duplicated(keep='first')]

    return df

# Define project directories
script_dir        = Path(__file__).resolve().parent
project_root      = script_dir.parent
dataset_root      = project_root / 'dataset_1st_trim'
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

        # Debug: inspect columns and ranges
        print(f"Processing sample {sample}, point {point}")
        print(f"ON range: {sig.index.min()} to {sig.index.max()}")
        print(f"OFF range: {noise.index.min()} to {noise.index.max()}")

        if 'AMP' not in sig.columns or 'AMP' not in noise.columns:
            print(f"AMP column missing in files; skipping {on_file.name}")
            continue

        sig['AMP'] = pd.to_numeric(sig['AMP'], errors='coerce')
        noise['AMP'] = pd.to_numeric(noise['AMP'], errors='coerce')
        
        # Align noise AMP to signal's timestamp grid, filling missing with 0
        noise_amp_aligned = noise['AMP'].reindex(sig.index).fillna(0)

        # Subtract only the 'AMP' channel
        clean = sig.copy()
        clean['AMP'] = sig['AMP'] - noise_amp_aligned

        # Save cleaned CSV including all other columns
        out_path = out_sub / f"{on_file.name}"
        clean.to_csv(out_path, index_label='Timestamp')
        print(f"Saved cleaned AMP to {out_path}")

print("Noise removal (AMP only) complete.")
exec(open('3snippet.py').read())