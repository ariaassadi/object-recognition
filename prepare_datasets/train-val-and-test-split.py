import os
import shutil
import random

# Set the base directory for images and labels
base_directory = '../../../../..//mimer/NOBACKUP/groups/snic2022-23-105/processed_data/'

# Directories for images and labels
image_directory = os.path.join(base_directory, 'images/dataset_big')
label_directory = os.path.join(base_directory, 'labels/dataset_big')

# Directories for the split datasets
train_dir = 'train_big'
val_dir = 'val_big'
test_dir = 'test'

# Ratios for splitting (e.g., 70% train, 15% val, 15% test)
train_ratio = 0.70
val_ratio = 0.15

# Set random seed for reproducibility
random.seed(42)

# Create directories if they don't exist
for dir in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(base_directory, 'images', dir), exist_ok=True)
    os.makedirs(os.path.join(base_directory, 'labels', dir), exist_ok=True)

# Get all file names (assuming image and label filenames are the same, minus extension)
all_files = [os.path.splitext(f)[0] for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
random.shuffle(all_files)

# Split files into train, val, test
num_train = int(len(all_files) * train_ratio)
num_val = int(len(all_files) * val_ratio)

train_files = all_files[:num_train]
val_files = all_files[num_train:num_train + num_val]
test_files = all_files[num_train + num_val:]

# Function to copy files
def copy_files(files, source_image_dir, source_label_dir, target_image_dir, target_label_dir):
    for f in files:
        shutil.copy(os.path.join(source_image_dir, f + '.jpg'), os.path.join(target_image_dir, f + '.jpg'))
        shutil.copy(os.path.join(source_label_dir, f + '.txt'), os.path.join(target_label_dir, f + '.txt'))

# Copy files to their respective directories
copy_files(train_files, image_directory, label_directory, os.path.join(base_directory, 'images', train_dir), os.path.join(base_directory, 'labels', train_dir))
copy_files(val_files, image_directory, label_directory, os.path.join(base_directory, 'images', val_dir), os.path.join(base_directory, 'labels', val_dir))
copy_files(test_files, image_directory, label_directory, os.path.join(base_directory, 'images', test_dir), os.path.join(base_directory, 'labels', test_dir))

print("Dataset copied into train_big, val_big, and test sets.")
