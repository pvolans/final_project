from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import datetime

class DatasetSnipper:
    def __init__(self):
        self.script_dir = Path(__file__).resolve().parent
        self.project_root = self.script_dir.parent
        self.input_root = self.project_root / 'dataset_clean'
        self.output_root = self.project_root / 'dataset_snipped'
        self.output_root.mkdir(exist_ok=True)

        # Parameters
        self.expected_period = 0.0174  # seconds
        self.glitch_threshold = 0.18   # seconds

    def snip_file(self, input_file: Path, output_file: Path):
        df = pd.read_csv(input_file)

        if 'Timestamp' not in df.columns:
            print(f"Skipping {input_file.name}: Missing 'Timestamp' column")
            return

        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        df['dt_raw'] = df['Timestamp'].diff().dt.total_seconds().fillna(0)
        
        df['dt_fixed'] = df['dt_raw'].where(df['dt_raw'] <= self.glitch_threshold, self.expected_period)
        df['Timestamp'] = df['dt_fixed'].cumsum()

        start_time = pd.Timestamp("2025-06-03 09:00:00")
        df['Timestamp'] = start_time + pd.to_timedelta(df['Timestamp'], unit='s')
        # Drop helper columns before saving (preserve original column layout)
        df.drop(columns=['dt_raw', 'dt_fixed'], inplace=True)

        # Save snipped data with original columns (including Timestamp)
        df.to_csv(output_file, index=False)
        print(f"Saved snipped file: {output_file.relative_to(self.output_root.parent)}")

    def process_all(self):
        for subdir in self.input_root.glob('dataset_*'):
            if not subdir.is_dir():
                continue

            out_subdir = self.output_root / f"{subdir.name}_snipped"
            out_subdir.mkdir(parents=True, exist_ok=True)

            for file in subdir.glob('*.csv'):
                out_file = out_subdir / file.name
                self.snip_file(file, out_file)

        print("All files processed and saved to 'dataset_snipped'.")

if __name__ == '__main__':
    snipper = DatasetSnipper()
    snipper.process_all()
