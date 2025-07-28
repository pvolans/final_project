import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import random

class TimeSeriesPlotter:
    def __init__(self):
        self.script_dir = Path(__file__).resolve().parent
        self.project_root = self.script_dir.parent
        self.dataset_root = self.project_root / 'dataset_preprocessed'

    def find_dataset_folders(self):
        """Find all dataset folders matching the pattern dataset_*"""
        if not self.dataset_root.exists():
            print(f"Dataset root not found: {self.dataset_root}")
            return []

        pattern = "dataset_2025-06-15_13-10-29*"
        folders = list(self.dataset_root.glob(pattern))
        return sorted(folders)

    def load_csv_file(self, file_path):
        """Load a single CSV file and return DataFrame"""
        try:
            df = pd.read_csv(file_path)
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None

    def collect_signal_files(self, max_signals=1, randomize=True):
        """Collect signal files from dataset folders"""
        dataset_folders = self.find_dataset_folders()
        all_signal_files = []

        for folder in dataset_folders:
            csv_files = list(folder.glob("data_4_11.csv"))
            for csv_file in csv_files:
                parts = csv_file.stem.split('_')
                if len(parts) >= 3:
                    class_id = parts[1]
                    signal_num = parts[2]
                    all_signal_files.append({
                        'path': csv_file,
                        'class_id': class_id,
                        'signal_num': signal_num,
                        'folder': folder.name
                    })

        if randomize:
            random.shuffle(all_signal_files)
            print(f"Randomized {len(all_signal_files)} available files")

        return all_signal_files[:max_signals]

    def plot_single_file_from_dataset(self, signal_type='AMP', figsize=(12, 5)):
        """Plot a single random signal file"""
        signal_files = self.collect_signal_files(max_signals=1, randomize=True)

        if not signal_files:
            print("No signal files found!")
            return

        signal_info = signal_files[0]
        print(f"Selected file: {signal_info['folder']}/data_{signal_info['class_id']}_{signal_info['signal_num']}.csv")

        df = self.load_csv_file(signal_info['path'])

        if df is None or signal_type not in df.columns:
            print(f"{signal_type} column not found in the file.")
            return

        # Plot
        plt.figure(figsize=figsize)
        plt.plot(df['Timestamp'], df[signal_type], color='blue', linewidth=1)
        plt.title(f"{signal_type} - Class {signal_info['class_id']}, Signal {signal_info['signal_num']} ({signal_info['folder']})", fontsize=12)
        plt.xlabel('Time')
        plt.ylabel(signal_type)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Usage example
if __name__ == "__main__":
    plotter = TimeSeriesPlotter()
    plotter.plot_single_file_from_dataset(signal_type='AMP')