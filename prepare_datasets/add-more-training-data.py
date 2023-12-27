import os
import shutil

# Folder paths
folder1 = 'Mimmi Gustafsson/Stadens ansikten Mimmi Gustafsson del 2'
folder2 = 'Mimmi Gustafsson/Mimmi Gustafsson Stadens ansikten'
folder3 = 'Mimmi Gustafsson/Stadens ansikten Mimmi Gustafsson MG 101 - 2190'
train_folder = 'processed_data/images/train/'
val_folder = 'processed_data/images/val/'
output_folder = 'processed_data/images/dataset_big/'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to get set of file names in a folder
def get_filenames(folder_path):
    return set(os.listdir(folder_path))

# Get filenames in train and val folders
train_filenames = get_filenames(train_folder)
val_filenames = get_filenames(val_folder)

# Function to copy unique files to the output folder
def copy_unique_files(source_folder):
    for filename in os.listdir(source_folder):
        # Skip file if it exists in train or val folders
        if filename in train_filenames or filename in val_filenames:
            continue

        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(output_folder, filename)

        # Check if file already exists in the output folder
        if not os.path.exists(dest_path):
            shutil.copy2(src_path, dest_path)

# Process each folder
copy_unique_files(folder1)
copy_unique_files(folder2)
copy_unique_files(folder3)

print("Photos combined successfully.")