% MATLAB Script to process CSV files, apply Welch's method, and save graphs

% Get the current script directory
scriptDir = fileparts(mfilename('fullpath'));

% Create a folder to save graphs if it doesn't exist
graphFolder = fullfile(scriptDir, 'Graph');
if ~exist(graphFolder, 'dir')
    mkdir(graphFolder);
end

% List of CSV files to process
csvFiles = arrayfun(@(y) fullfile(scriptDir, sprintf('data_8_%d_L.csv', y)), 1:6, 'UniformOutput', false);

for i = 1:length(csvFiles)
    csvFile = csvFiles{i};
    try
        % Read the CSV file
        data = readtable(csvFile);

        % Ensure Timestamp is parsed correctly
        data.Timestamp = datetime(data.Timestamp, 'InputFormat', 'yyyy-MM-dd HH:mm:ss.SSS');

        % Calculate average sampling rate
        timeDiffs = seconds(diff(data.Timestamp)); % Time differences in seconds
        avgSamplingRate = 1 / mean(timeDiffs);     % Average sampling rate in Hz

        fprintf('Average Sampling Rate: %.2f Hz\n', avgSamplingRate);

        % Extract the AMP column
        ampSeries = data.AMP;

        % Apply Welch's method
        [psd, freqs] = pwelch(ampSeries, hanning(512), 256, 512, avgSamplingRate);

        % Plot the results
        figure;
        semilogy(freqs, psd);
        xlim([0 30]);  % Match Python axis limits
        % ylim([1e-3 1e1]);  % Match Python y-axis limits

        title(sprintf("Welch's Method - %s\n(Sampling Rate: %.2f Hz)", extractBefore(csvFile, '.'), avgSamplingRate));
        grid on;
        set(gca, 'FontSize', 12); % Match Python font size
        xlabel('Frequency (Hz)');
        ylabel('Power Spectral Density');
        % Save the plot
        [~, baseFilename, ~] = fileparts(csvFile); % Extract the base filename without path or extension
        graphPath = fullfile(graphFolder, sprintf('welch_%s.png', baseFilename));
        saveas(gcf, graphPath, 'png'); % Ensure consistent image format
        close;

        fprintf('Graph saved for %s: %s\n', csvFile, graphPath);

    catch ME
        fprintf('Error processing file %s: %s\n', csvFile, ME.message);
    end
end
