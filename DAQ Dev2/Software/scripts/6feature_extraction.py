import os
import pandas as pd
import numpy as np
from scipy.signal import welch
import pywt
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def extract_yule_walker_features(signal_data, ar_order=15):
    try:
        signal_centered = signal_data - np.mean(signal_data)
        autocorr = np.correlate(signal_centered, signal_centered, mode='full')
        autocorr = autocorr[autocorr.size // 2:]
        autocorr = autocorr / autocorr[0]
        R = autocorr[:ar_order]
        r = autocorr[1:ar_order+1]
        toeplitz_matrix = np.array([R[abs(i-j)] for i in range(ar_order) for j in range(ar_order)]).reshape(ar_order, ar_order)
        ar_coeffs = np.linalg.solve(toeplitz_matrix, r)
        error_var = autocorr[0] * (1 - np.sum(ar_coeffs * r))
        n = len(signal_data)
        log_likelihood = -0.5 * n * np.log(2 * np.pi * error_var) - 0.5 * n
        aic = -2 * log_likelihood + 2 * ar_order
        bic = -2 * log_likelihood + ar_order * np.log(n)
        features = {
            **{f'ar_coeff_{i+1}': coeff for i, coeff in enumerate(ar_coeffs)},
            'ar_variance': error_var,
            'ar_aic': aic,
            'ar_bic': bic
        }
        return features
    except Exception as e:
        print(f"Error in Yule-Walker AR: {e}")
        return {f'ar_coeff_{i+1}': 0 for i in range(ar_order)}

def extract_welch_features(signal_data, fs=500, nperseg=128):
    try:
        frequencies, psd = welch(signal_data, fs=fs, nperseg=nperseg)
        total_power = np.sum(psd)
        probs = psd / total_power
        features = {
            'welch_total_power': total_power,
            'welch_mean_freq': np.sum(frequencies * psd) / total_power,
            'welch_median_freq': frequencies[np.argmax(np.cumsum(psd) >= total_power/2)],
            'welch_peak_freq': frequencies[np.argmax(psd)],
            'welch_peak_power': np.max(psd),
            'welch_spectral_rolloff': frequencies[np.argmax(np.cumsum(psd) >= 0.85 * total_power)],
            'welch_spectral_flux': np.sum(np.diff(psd)**2),
            'welch_spectral_entropy': -np.sum(probs * np.log2(probs + 1e-12))
        }
        bands = {'delta': (0,4), 'theta':(4,8), 'alpha':(8,13), 'beta':(13,25)}
        for name, (low, high) in bands.items():
            mask = (frequencies>=low)&(frequencies<=high)
            features[f'welch_{name}_power'] = np.sum(psd[mask])
        return features
    except Exception as e:
        print(f"Error in Welch method: {e}")
        return {'welch_total_power': 0}

def extract_wavelet_features(signal_data, wavelet='db4', levels=6):
    try:
        coeffs = pywt.wavedec(signal_data, wavelet, level=levels)
        features = {}
        a = coeffs[0]
        e = np.sum(a**2)
        features.update({
            'wavelet_approx_mean': np.mean(a),
            'wavelet_approx_std': np.std(a),
            'wavelet_approx_var': np.var(a),
            'wavelet_approx_energy': e,
            'wavelet_approx_entropy': -np.sum((a**2/e)*np.log2(a**2/e+1e-12))
        })
        all_energy = e
        for level, d in enumerate(coeffs[1:],1):
            e_l = np.sum(d**2)
            all_energy += e_l
            features.update({
                f'wavelet_detail_{level}_mean': np.mean(d),
                f'wavelet_detail_{level}_std': np.std(d),
                f'wavelet_detail_{level}_var': np.var(d),
                f'wavelet_detail_{level}_energy': e_l,
                f'wavelet_detail_{level}_entropy': -np.sum((d**2/e_l)*np.log2(d**2/e_l+1e-12))
            })
        for idx, c in enumerate(coeffs):
            rel = np.sum(c**2)/all_energy
            features[f'wavelet_rel_energy_{idx}'] = rel
        features['wavelet_total_energy'] = all_energy
        return features
    except Exception as e:
        print(f"Error in Wavelet Transform: {e}")
        return {'wavelet_total_energy': 0}

def process_single_file(file_path, output_dir_spectral, output_dir_wavelets, sample_id, dataset_id):
    try:
        df = pd.read_csv(file_path)
        required = ['AMP','DIST','Angle','ON','Movement','Timestamp']
        if any(col not in df.columns for col in required):
            print(f"Missing cols in {file_path.name}")
            return False

        amp = df['AMP'].values
        # Metadata removed from output
        md = {k: df[k].iloc[0] for k in ['TEMP', 'Movement']}
        spec = {**extract_yule_walker_features(amp), **extract_welch_features(amp), **md}
        wave = {**extract_wavelet_features(amp), **md}

        name_parts = Path(file_path).stem.split('_')
        point = name_parts[2]

        spectral_filename = f"data_{sample_id}_{point}_{dataset_id}_spectral.csv"
        wavelets_filename = f"data_{sample_id}_{point}_{dataset_id}_wavelets.csv"

        pd.DataFrame([spec]).to_csv(output_dir_spectral / spectral_filename, index=False)
        pd.DataFrame([wave]).to_csv(output_dir_wavelets / wavelets_filename, index=False)

        return True
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return False


def main():
    base_dir = Path(__file__).resolve().parent.parent
    pre_root = base_dir / 'dataset_preprocessed_with_interpolation'
    feature_root = base_dir / 'dataset_feature_extracted'

    dataset_id = 0

    for sub in sorted(pre_root.iterdir()): 
        if not sub.is_dir():
            print("There is no directory as a sub folder")
            print("There is no directory as a sub folder")
            continue

        for f in sorted(sub.glob('data_*.csv')):
            name_parts = f.stem.split('_')
            sample_id = name_parts[1]

            # NEW STRUCTURE
            sample_folder = feature_root / f"dataset_sample_{sample_id}"
            out_spec = sample_folder / 'dataset_spectral' 
            out_wave = sample_folder / 'dataset_wavelets'


            out_spec.mkdir(parents=True, exist_ok=True)
            out_wave.mkdir(parents=True, exist_ok=True)

            print(f"Processing {f.name} into {sample_folder.name} with dataset id {dataset_id}")
            process_single_file(f, out_spec, out_wave, sample_id, dataset_id)
            dataset_id += 1

    print("All processing finished.")

if __name__ == '__main__':
    main()