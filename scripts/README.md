These scripts are used to prepare the `datasets/` folder. If you use the virtual machines on Alvis, these steps are already executed.

# Step 1
### train-test-split.py
The folder `mimmi_chairs_labeled_data/` can be downloaded from Box. Before running the scripts, please make sure that your file structure looks like this:

```
datasets
├── mimmi_chairs_labeled_data
│   ├── classes.txt
│   ├── images
│   ├── labels
│   └── notes.json
└── train-and-test-split.py

```
This script should create a new folder called `processed_data/`

# Step 2
### 