# Instructions
These scripts are used to prepare the `datasets/` folder. If you use the virtual machines on Alvis, these steps are already executed.

## Step 1
Create an empty directory called `datasets/` and put the scripts of this folder inside `datasets/`.

## Step 2
### train-and-val-split.py
The folder `mimmi_chairs_labeled_data/` can be downloaded from Box. Before running the script `train-and-val-split.py`, please make sure that your file structure looks like this:

```
datasets
├── mimmi_chairs_labeled_data
│   ├── classes.txt
│   ├── images
│   ├── labels
│   └── notes.json
└── train-and-val-split.py
```
This script should create a new folder called `processed_data/`

## Step 3
### add-more-training-data.py
The folder `Mimmi Gustafsson/` can be downloaded from Box. Before running the script `add-more-training-data.py`, please make sure that your file structure looks like this:

```
datasets
├── Mimmi Gustafsson
│   ├── Mimmi Gustafsson Stadens ansikten
│   ├── Stadens ansikten Mimmi Gustafsson del 2
│   └── Stadens ansikten Mimmi Gustafsson MG 101 - 2190
├── processed_data
│   ├── images
│   └── labels
└── train-and-val-split.py
```
This script should create a new folder called `processed_data/images/train_big`.

## Step 4
Copy the folder `processed_data/images/train_big` to the store space on Alvis.

## Step 5
Execute the NN-model to predicts labels and store them in `processed_data/labels/dataset_big_old`. Copy the results to `processed_data/labels/dataset_big`.

## Step 6
Manually adjust all the labels in `processed_data/labels/dataset_big`. This can be done by using label-studio.

## Step 7
### train-val-val-test-split.py
This will create new folders for training, testing, and validating the model. 

## Step 8
The preparation for `datasets/` is completed. The model can now be trained on the big training dataset.
