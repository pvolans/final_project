import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import numpy as np
import random

class TimeSeriesPlotter:
    def __init__(self):
        # Use Path to find folders
        self.script_dir = Path(__file__).resolve().parent
        self.project_root = self.script_dir.parent
        self.dataset_root = self.project_root / 'dataset_preprocessed_with_interpolation'
        self.signals_data = []
        
    def find_dataset_folders(self):
        """Find all dataset folders matching the pattern dataset_2025-05-*"""
        if not self.dataset_root.exists():
            print(f"Dataset root not found: {self.dataset_root}")
            return []
        
        # Find folders matching pattern dataset_2025-05-*
        pattern = "dataset_*"
        folders = list(self.dataset_root.glob(pattern))
        return sorted(folders)
    
    def load_csv_file(self, file_path):
        """Load a single CSV file and return DataFrame"""
        try:
            df = pd.read_csv(file_path)
            # Convert timestamp to datetime
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None
    
    def collect_signal_files(self, max_signals=9, randomize=True):
        """Collect signal files from dataset folders"""
        dataset_folders = self.find_dataset_folders()
        all_signal_files = []
        
        # First collect ALL available files
        for folder in dataset_folders:
            # Find all CSV files in the folder
            csv_files = list(folder.glob("data_*.csv"))
            
            for csv_file in csv_files:
                # Extract class_id and signal_num from filename
                filename = csv_file.stem  # filename without extension
                # Split by underscore
                parts = filename.split('_')
                if len(parts) >= 3:
                    class_id = parts[1]
                    signal_num = parts[2]
                    all_signal_files.append({
                        'path': csv_file,
                        'class_id': class_id,
                        'signal_num': signal_num,
                        'folder': folder.name
                    })
        
        # Randomize if requested
        if randomize:
            random.shuffle(all_signal_files)
            print(f"Randomized {len(all_signal_files)} available files")
        
        return all_signal_files[:max_signals]
    
    def plot_signals(self, signals=['AMP'], figsize=(15, 12), randomize=True):
        """Plot 9 time-series signals in a 3x3 grid - AMP only"""
        signal_files = self.collect_signal_files(9, randomize=randomize)
        
        if not signal_files:
            print("No signal files found!")
            return
        
        print(f"Selected files for plotting:")
        for i, signal_info in enumerate(signal_files):
            print(f"  {i+1}. {signal_info['folder']}/data_{signal_info['class_id']}_{signal_info['signal_num']}.csv")
        
        # Create subplots
        fig, axes = plt.subplots(3, 3, figsize=figsize)
        axes = axes.flatten()  # Flatten for easier indexing
        
        for i, signal_info in enumerate(signal_files):
            df = self.load_csv_file(signal_info['path'])
            
            if df is None:
                continue
                
            ax = axes[i]
            
            # Plot AMP signal only
            if 'AMP' in df.columns:
                ax.plot(df['Timestamp'], df['AMP'], 
                       color='blue', alpha=0.8, linewidth=1)
            
            # Formatting
            ax.set_title(f"AMP - Class {signal_info['class_id']}, Signal {signal_info['signal_num']}\n"
                        f"({signal_info['folder']})", fontsize=10)
            ax.set_xlabel('Time', fontsize=8)
            ax.set_ylabel('AMP', fontsize=8)
            ax.grid(True, alpha=0.3)
            
            # Rotate x-axis labels for better readability
            ax.tick_params(axis='x', rotation=45, labelsize=8)
            ax.tick_params(axis='y', labelsize=8)
        
        # Hide empty subplots if we have fewer than 9 signals
        for i in range(len(signal_files), 9):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        title = 'Random AMP Signal Analysis (9 Signals)' if randomize else 'AMP Signal Analysis (9 Signals)'
        plt.suptitle(title, fontsize=16, y=0.98)
        plt.show()
    
    def plot_single_signal_type(self, signal_type='AMP', figsize=(15, 12), randomize=True):
        """Plot a single signal type across 9 different files"""
        signal_files = self.collect_signal_files(9, randomize=randomize)
        
        if not signal_files:
            print("No signal files found!")
            return
        
        print(f"Selected files for {signal_type} plotting:")
        for i, signal_info in enumerate(signal_files):
            print(f"  {i+1}. {signal_info['folder']}/data_{signal_info['class_id']}_{signal_info['signal_num']}.csv")
        
        fig, axes = plt.subplots(3, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, signal_info in enumerate(signal_files):
            df = self.load_csv_file(signal_info['path'])
            
            if df is None or signal_type not in df.columns:
                continue
                
            ax = axes[i]
            ax.plot(df['Timestamp'], df[signal_type], 
                   color='blue', linewidth=1)
            
            ax.set_title(f"{signal_type} - Class {signal_info['class_id']}, Signal {signal_info['signal_num']}", 
                        fontsize=10)
            ax.set_xlabel('Time', fontsize=8)
            ax.set_ylabel(signal_type, fontsize=8)
            ax.grid(True, alpha=0.3)
            ax.tick_params(axis='x', rotation=45, labelsize=8)
            ax.tick_params(axis='y', labelsize=8)
        
        # Hide empty subplots
        for i in range(len(signal_files), 9):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        title = f'Random {signal_type} Signal Analysis Across 9 Files' if randomize else f'{signal_type} Signal Analysis Across 9 Files'
        plt.suptitle(title, fontsize=16, y=0.98)
        plt.show()
    
    def print_dataset_info(self):
        """Print information about available datasets and files"""
        print("Path Information:")
        print("=" * 50)
        print(f"Script directory: {self.script_dir}")
        print(f"Project root: {self.project_root}")
        print(f"Dataset root: {self.dataset_root}")
        print(f"Dataset root exists: {self.dataset_root.exists()}")
        
        signal_files = self.collect_signal_files(50, randomize=False)  # Get more files for info, don't randomize for info
        
        print("\nDataset Information:")
        print("=" * 50)
        
        folders = {}
        for signal_info in signal_files:
            folder = signal_info['folder']
            if folder not in folders:
                folders[folder] = []
            folders[folder].append(f"data_{signal_info['class_id']}_{signal_info['signal_num']}.csv")
        
        for folder, files in folders.items():
            print(f"\n{folder}:")
            for file in sorted(files):
                print(f"  - {file}")
        
        print(f"\nTotal files found: {len(signal_files)}")
        
        # Set random seed for reproducible randomization (optional)
        random.seed(42)
        print(f"Random seed set to 42 for reproducible results")

# Usage example
if __name__ == "__main__":
    # Initialize plotter
    plotter = TimeSeriesPlotter()
    
    # Print dataset information
    plotter.print_dataset_info()
    
    # Plot 9 RANDOM signals with AMP only
    print("\nPlotting 9 RANDOM signals with AMP only...")
    plotter.plot_signals(randomize=True)
    
    # Alternative: Use the single signal method for random AMP files
    print("\nAlternative: Plotting AMP signal from 9 RANDOM files...")
    plotter.plot_single_signal_type('AMP', randomize=True)
    
    # If you want sequential (non-random) files, set randomize=False
    print("\nFor comparison - Sequential files (first 9 found):")
    plotter.plot_signals(randomize=False)