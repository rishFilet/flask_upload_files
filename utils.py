import os
from config import EnvStrings

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in os.getenv(EnvStrings.ALLOWED_EXTENSIONS.value)


def check_dir_path(dir_name=os.getenv(EnvStrings.UPLOAD_FOLDER.value)):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def check_file_exists(filename, dir_name=os.getenv(EnvStrings.UPLOAD_FOLDER.value)):
    if os.path.exists(f"{dir_name}/{filename}"):
        return True
    else:
        return False
