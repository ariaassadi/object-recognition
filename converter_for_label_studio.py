from label_studio_converter.imports import yolo
import json


def convert_yolo_to_ls(data_dir, json_file_name='converted_data.json'):
    """
    This function converts YOLO formatted datasets into formats that label-studio can import.
    It takes in a directory that should be the top level directory of your YOLO data.
        Such directories should contain 2 subdirectories, one called 'images' and one called 'labels'.
        The image directory should contain images and the labels directory should contain .txt files that
        correspond to the image names in the image directory.
        'data_dir' should also contain a file called 'classes.txt' that contains an alphabetically ordered list
        of all the classes used for this dataset.

    This function converts the YOLO data into a .JSON file that can be used in label-studio.
    When this conversion happens the paths to the images are not correctly inserted into the .JSON files.
    To fix that this scripts reopens the .JSON file that it generated and replaces all paths to the images with
    their full path. Without doing this it can be very tricky to import the data into label-studio.
    """

    # In case we are missing a trailing slash in our data directory.
    if data_dir[-1] != '/':
        data_dir = data_dir + '/'

    # In case we are missing the .json from the JSON file.
    if '.json' not in json_file_name:
        json_file_name = json_file_name + '.json'

    # This converts the data YOLO data into a .json file that label-studio can read.
    # The problem is that it tends to mess up the path to the images so we will need to fix that.
    yolo.convert_yolo_to_ls(input_dir=data_dir, out_file=json_file_name)

    # Read the .json file we just created so that we can fix the paths.
    with open(json_file_name, 'r') as json_input:
        json_file = json.load(json_input)

    # The path to the images is not full path. Here we switch it out to the full path.
    # We assume that this full path is the data_dir/images
    for x in json_file:
        img_name = x['data']['image'].split('/')[-1]
        x['data']['image'] = '/data/local-files/?d=' + data_dir + 'images/' + img_name

    with open(json_file_name, 'w') as outfile:  # Write the data again, now with the correct paths to the images.
        json.dump(json_file, outfile)


if __name__ == '__main__':
    data_location = r'G:\my_folder\mimmi_chairs_labeled_data'
    convert_yolo_to_ls(data_location)
