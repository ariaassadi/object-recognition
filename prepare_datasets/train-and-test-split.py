import os
import shutil
import random

# This script is used to split a folder with images, and thier corresponding labels, to a new folder with a train and test set

# Base directories
original_data_dir = 'mimmi_chairs_labeled_data'     # The name of the folder containing the images/ and labels/ folder
processed_data_dir = 'processed_data'               # The name of the new folder that this script will create

# Set the seed for reproducibility
random.seed(42)

# Subdirectories for images and labels
original_images_dir = os.path.join(original_data_dir, 'images')
original_labels_dir = os.path.join(original_data_dir, 'labels')
processed_images_dir = os.path.join(processed_data_dir, 'images')
processed_labels_dir = os.path.join(processed_data_dir, 'labels')

# Create train/val directories inside processed_data/
for subdir in ['train', 'val']:
    for dir in [processed_images_dir, processed_labels_dir]:
        os.makedirs(os.path.join(dir, subdir), exist_ok=True)

# Get a list of filenames (without extension)
files = [os.path.splitext(file)[0] for file in os.listdir(original_images_dir) if file.endswith('.jpg')]

# Shuffle and split
random.shuffle(files)
split_idx = int(0.8 * len(files))  # 80% for training
train_files = files[:split_idx]
val_files = files[split_idx:]

# Function to move files
def move_files(file_list, source_images, source_labels, dest_images, dest_labels):
    for file in file_list:
        shutil.move(os.path.join(source_images, file + '.jpg'),
                    os.path.join(dest_images, file + '.jpg'))
        shutil.move(os.path.join(source_labels, file + '.txt'),
                    os.path.join(dest_labels, file + '.txt'))

# Move files to respective directories in processed_data/
move_files(train_files, original_images_dir, original_labels_dir, os.path.join(processed_images_dir, 'train'), os.path.join(processed_labels_dir, 'train'))
move_files(val_files, original_images_dir, original_labels_dir, os.path.join(processed_images_dir, 'val'), os.path.join(processed_labels_dir, 'val'))

print("Photos moved successfully.")