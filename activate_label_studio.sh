# Activates the virtual environment that has label-studio installed
source venv/Scripts/activate &&

# Allows label-studio to use local files.
export LOCAL_FILES_SERVING_ENABLED=true &&

# Sets what hard drive your local files are located in, very important if you are using Windows.
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=C:\\ &&

# Runs label-studio
label-studio
