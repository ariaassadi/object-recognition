## Instructions
In order to train the model, you need to have a folder in the same directory as the GitHub repo, called `datasets/`, with the data of images and their corresponding labels. Your data structure should look like this:

```
├── datasets
│   ├── mimmi_chairs_labeled_data
│   │   ├── classes.txt
│   │   ├── images
│   │   ├── labels
│   │   └── notes.json
│   └── train-and-test-split.py
└── object-recognition
    ├── dataset.yaml
    └── <other-contents-in-the-GitHub-repo>
```
Note: The folder "mimmi_chairs_labeled_data" can be downloaded from Box, and a copy of "train-and-test-split.py" is stored on GitHub (`object-recognition/scripts`).
Before executing the code, please go to `datasets/` and run `train-and-test-split.py`.

### Requirements
Please make sure to install all the required packages in `requirements.txt` with `pip install`, preferably in a virtual environment.
