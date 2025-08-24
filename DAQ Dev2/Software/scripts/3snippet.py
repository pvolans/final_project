from pathlib import Path
import pandas as pd
import numpy as np

class DatasetSnipper:
    def __init__(self):
        self.script_dir = Path(__file__).resolve().parent
        self.project_root = self.script_dir.parent
        self.input_root = self.project_root / 'dataset_clean'
        self.output_root = self.project_root / 'dataset_short_snipped'
        self.output_root.mkdir(exist_ok=True)

        # Parameters
        self.expected_period = 0.0174  # seconds
        self.glitch_threshold = 0.18   # seconds

        # Base timestamp used for renumbering each snippet
        self.start_time = pd.Timestamp("2025-06-03 09:00:00")

    def snip_file(self, input_file: Path, output_dir: Path):
        df = pd.read_csv(input_file)

        if 'Timestamp' not in df.columns:
            print(f"Skipping {input_file.name}: Missing 'Timestamp' column")
            return

        # Parse timestamps robustly: coerce unparseable values (e.g. 'True'/'False') to NaT
        df['Timestamp_parsed'] = pd.to_datetime(df['Timestamp'], errors='coerce', infer_datetime_format=True)

        # Identify rows with valid timestamps
        valid_mask = ~df['Timestamp_parsed'].isna()
        if valid_mask.sum() == 0:
            print(f"Skipping {input_file.name}: no valid timestamps after parsing")
            return

        # Work on the sequence of valid rows to compute time diffs
        valid_positions = np.flatnonzero(valid_mask)
        times = df.loc[valid_mask, 'Timestamp_parsed'].reset_index(drop=True)

        # raw time differences in seconds for the valid series
        dt_raw_valid = times.diff().dt.total_seconds().fillna(0)

        # find break points in the valid series: break between i-1 and i when dt > threshold
        breaks_valid = np.where(dt_raw_valid > self.glitch_threshold)[0]

        # build segment start/end pairs in terms of the valid-series indices
        starts_valid = [0] + breaks_valid.tolist()
        ends_valid = breaks_valid.tolist() + [len(times)]

        for seg_idx, (vstart, vend) in enumerate(zip(starts_valid, ends_valid)):
            # map valid-series slice back to original dataframe row positions
            rows = valid_positions[vstart:vend]
            seg = df.iloc[rows].copy()
            if seg.empty:
                continue

            # get the dt_raw for this segment from the valid dt array
            dt_raw_seg = dt_raw_valid[vstart:vend].to_numpy()

            # Replace large dt values with expected_period
            dt_fixed_seg = np.where(dt_raw_seg <= self.glitch_threshold, dt_raw_seg, self.expected_period)

            # Ensure the first dt in a segment is zero (start of snippet)
            if len(dt_fixed_seg) > 0:
                dt_fixed_seg[0] = 0.0

            # --- NEW: use the original segment start time as base ---
            base_time = times.iloc[vstart]  # original real time when this snippet starts

            # Build new timestamps for this segment starting at the segment's original start time
            #seg['Timestamp'] = (base_time + pd.to_timedelta(pd.Series(dt_fixed_seg).cumsum(), unit='s'))

            # OPTIONAL: keep a copy of the original (string) Timestamp column if you'd like
            seg['Timestamp'] = seg['Timestamp_parsed']  # or df.loc[rows, 'Timestamp']

            # Drop helper parsed timestamp column before saving (preserve original column layout)
            seg = seg.drop(columns=[c for c in ['Timestamp_parsed'] if c in seg.columns])

            # Output filename: {original_stem}_{segment_index}{suffix} -> e.g. data_0_12_0.csv
            out_name = f"{input_file.stem}_{seg_idx}{input_file.suffix}"
            out_path = output_dir / out_name
            seg.to_csv(out_path, index=False)
            print(f"Saved snipped file: {out_path.relative_to(self.output_root.parent)}")

    def process_all(self):
        for subdir in self.input_root.glob('dataset_*'):
            if not subdir.is_dir():
                continue

            out_subdir = self.output_root / f"{subdir.name}_snipped"
            out_subdir.mkdir(parents=True, exist_ok=True)

            for file in subdir.glob('*.csv'):
                self.snip_file(file, out_subdir)

        print("All files processed and saved to 'dataset_short_snipped'.")

if __name__ == '__main__':
    snipper = DatasetSnipper()
    snipper.process_all()
    # continue pipeline if needed
    try:
        exec(open('4interpolation_of_data.py').read())
    except FileNotFoundError:
        print("4interpolation_of_data.py not found; skipping execution.")
