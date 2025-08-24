import pandas as pd
from pathlib import Path

# Function to load interpolated CSVs
def load_uniform(file_path):
    df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
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
dataset_root = project_root / 'dataset_interpolated'
pre_processed   = project_root / 'dataset_preprocessed_with_interpolation'
pre_processed.mkdir(exist_ok=True)

# -------------------- #
# Collect statistics
# -------------------- #
all_lengths = []
file_count = 0
COLUMNS = ['Timestamp', 'DIST', 'AMP', 'TEMP', 'VOLT', 'Angle', 'ON', 'Movement']

# Collect lengths and file info
records = []  # list of dicts: {'length': int, 'subdir': str, 'file': str, 'path': Path}
file_count = 0

for sub in dataset_root.iterdir():
    if not sub.is_dir():
        continue
    for f in sorted(sub.glob('data_*.csv')):
        try:
            df = load_uniform(f)
        except Exception as e:
            print(f"Error reading {sub.name}/{f.name}: {e}")
            continue

        if 'Timestamp' in df.columns:
            df = df.drop(columns=['Timestamp'])

        for c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

        numeric = df.select_dtypes(include='number')
        length = len(df)

        row = {
            'subdir': sub.name,
            'file': f.name,
            'path': str(f.resolve()),
            'length': length
        }

        for col in numeric.columns:
            row[f'{col}_mean'] = numeric[col].mean(skipna=True)
            row[f'{col}_std']  = numeric[col].std(skipna=True)

        records.append(row)


if not records:
    print("No valid files found under", dataset_root)
    raise SystemExit(1)

stats_df = pd.DataFrame(records).sort_values(by='length').reset_index(drop=True)


# Print dataset summary
print("\n--- Dataset Summary ---")
print(f"Total files: {len(stats_df)}")
print(f"Standard Deviation of signal length: {int(stats_df['length'].std())}")
print(f"Mean of signal length: {int(stats_df['length'].mean())}")
print("------------------------\n")

# Print shortest / longest lists
n = 10
print("---- Shortest signals (up to 10) ----")
print(stats_df.head(n)[['length','subdir','file']].to_string(index=False))
print("\n---- Longest signals (up to 10) ----")
print(stats_df.tail(n)[['length','subdir','file']].sort_values(by='length', ascending=False).to_string(index=False))


# Prompt user for desired sample length
time_series_sample = int(input("Enter desired uniform signal length for trimming: "))

# -------------------- #
# Begin signal processing (fixed)
# -------------------- #
for sub in dataset_root.iterdir():
    if not sub.is_dir():
        continue

    out_sub = pre_processed / f"{sub.name}_trimmed"
    out_sub.mkdir(parents=True, exist_ok=True)

    # 1) Build lookup: key = (sample, point, snip_id)
    files = list(sub.glob('data_*.csv'))
    lookup = {}
    for f in files:
        parts = f.stem.split('_')
        if len(parts) != 4:
            print(f"Skipping unexpected filename format: {f.name}")
            continue
        _, sample, point, snip_id = parts
        try:
            key = (int(sample), int(point), int(snip_id))
        except ValueError:
            print(f"Skipping non-integer name parts: {f.name}")
            continue
        lookup[key] = f

    # 2) Process entries from lookup (separate loop)
    for (sample, point, snip_id), f in sorted(lookup.items()):
        # load file
        sig = load_uniform(f)

        # If too short -> SKIP (do not save)
        if len(sig) < time_series_sample:
            print(f"Too short: {f.name} (length={len(sig)}). Skipping.")
            continue

        print(f"Processing sample {sample}, point {point}, snip id {snip_id}")

        # check AMP column
        if 'AMP' not in sig.columns:
            print(f"AMP column missing in file; skipping {f.name}")
            continue

        # trim and save
        trimmed = trim_signal_symmetric(sig, time_series_sample)
        out_path = out_sub / f"{f.name}"
        trimmed.to_csv(out_path, index=False, header=True)
        print(f"Saved to {out_path}")
#exec(open('1noise_canceling.py').read())