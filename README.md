## Requirements
Please make sure to install all the required packages in `requirements.txt` with `pip install`, preferably in a virtual environment.

## Instructions
In order to train the model, you need to have a folder called `datasets/`, at the same level as the GitHub repository, with the relevant training and validation data. Instructions for how to prepare this folder, can be found in `prepare_datasets/`. When the preparation is done, the file structure should look like this:

```
├── datasets
│   ├── processed_data
│   │   ├── labels
│   │   └── images
│   ├── add-more-training-data.py
│   └── train-and-test-split.py
└── object-recognition
    └── <contents-in-this-GitHub-repo>
```

## Things left to do
1. Combine the three folders and delted duplicates
2. Remove all photos that are already labelled by Aron. Put the new photos in `processed_data/images/train_big`
3. Use the trained model to predict labels on `processed_data/images/train_big`. But the results in `processed_data/labels/train_big`.
4. Manually adjust the predicted labels to make `train_big` more realible
5. Train a new model with all the available training data (`train` and `train_big`)
6. Evaluate the results on `processed_data/images/val`
* Write the report
* Project presentation