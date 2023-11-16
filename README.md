# How to import data to label-studio

This is a tricky process that needs to be done in an exact way for it to work.
First, make sure that the 'LOCAL_FILES_SERVING_ENABLED' environment variable is set to 'true'.
If you are using windows then you also need to set the 'LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT' to the
hard drive letter where your images are contained. Otherwise it will not be able to locate your images.

This can all be done automatically with a script I created called 'activate_label-studio.sh'.
All that script needs is for you to makes sure that it has the correct path to the python virtual environment
that you are using and that that virtual environment has already installed the 'label-studio' python package.

Next is to use the 'converter_for_label_studio.py' file to convert the YOLO data into a format that label-studio
can import. In this script there is a function called 'convert_yolo_to_ls' that takes care of this for us.
This function needs the full path of the top level directory of the YOLO data as input.

Example: G:\my_folder\mimmi_chairs_labeled_data

This top level directory must have 2 folders, one called 'images' that contain the images and one called
'labels' that have the labeled data in text files. Each associated label data text file must have
the same name as the image it labels. In this directory must also be a text file called "classes.txt"
that has an alphabetical list of all of the classes.

Once you have successfully used the 'converter_for_label_studio.py' script you will end up with 2 files.
1. converted_data.json
2. converted_data.label_config.xml
These files can be used to import the data into label-studio.

The next step is to create a new project in label-studio. When the option comes for importing data import
the 'converted_data.json' file. Then in the 'Labeling setup' tab select 'Object Detection with Bounding Boxes'.
After that you should see an option for adding in the labels. There is a button for switching from visual input
to code input called 'Code | Visual'. You can click on the 'Code' button and then you should see a box for inserting XML.
copy everything from the 'converted_data.label_config.xml' file that you generated earlier and put it in this box. Then click 'Save'.

Now you have successfully created the project but you may notice that the images appear broken in label-studio. 
This happens because label-studio needs to know where your images are located.
You fix this by going into your label-studio project, select settings -> cloud storage -> add source storage
In the settings here you need to select 'local storage' for your 'storage type' and then add the directory that contains your images.
There is an option called 'Treat every bucket object as a source file' do NOT check it.
(don't worry though if you did, you can always uncheck it).
Once this is done there is an option to sync the local data, do NOT do that.

Once you have done all this everything should be working correctly.