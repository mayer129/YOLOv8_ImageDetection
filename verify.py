import os

# Path to the directory containing the images
dir_path = 'datasets/train/images'  # Update this path to the correct one

# Generate a set of all expected file names
expected_files = {f"{i:05}.jpeg" for i in range(1, 14001)}

# Read the actual files in the directory
actual_files = set(os.listdir(dir_path))

# Find missing files
missing_files = expected_files - actual_files

# Display missing files
print(missing_files)
