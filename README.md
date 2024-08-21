import os
import librosa
import soundfile as sf

# Path to the directory containing .wav files to process
input_path = r"C:\Users\nguye\OneDrive\바탕 화면\workspace\TaCoTron2"  #Input directory path
# Path to the directory where to store the processed .wav files
output_path = r"C:\Users\nguye\OneDrive\바탕 화면\workspace\output.txt"   # Output directory path

# Check that the output folder already exists, if it is not, create a new one
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Repeat through for all files in the input directory
for filename in os.listdir(input_path):
    # Check if the file has an extension of ".wav"
    if filename.endswith(".wav"):
        # Create the full path to the current .wav file
        filepath = os.path.join(input_path, filename)
        
        # Download the .wav file with a sample frequency of 22050 Hz
        y, sr = librosa.load(filepath, sr=22050)
        
        # Quiescing at the beginning and end of an audio file
        trimmed_audio, _ = librosa.effects.trim(y, top_db=20)
        
        # Normalize sound (brings sound amplitude to approximately [-1, 1])
        normalized_audio = librosa.util.normalize(trimmed_audio)
        
        # Create the full path to store the processed .wav file in the output directory
        output_filepath = os.path.join(output_path, filename)
        
        # Save the processed .wav file in 16-bit PCM format
        sf.write(output_filepath, normalized_audio, sr, subtype='PCM_16')

# Print a notification when processing is complete
print("All .wav files have been preprocessed and saved to the output folder.")
