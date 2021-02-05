import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from error_handling import *
from config import EnvStrings
from utils import *

app = Flask(__name__)
app.config.from_object(os.getenv(EnvStrings.APP_SETTINGS.value))
msg_obj = Msgs()

def upload_file(request):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            check_dir_path()
            if not check_file_exists(filename):
                msg_obj.add_success(MsgArea.UPLOAD_CSV,
                                    f"{file.filename} uploaded succssfully\nDownload from /uploads/{file.filename}")
            else:
                msg_obj.add_info(MsgArea.UPLOAD_CSV,
                                    f"{file.filename} already uploaded, replacing existing file")
            file.save(os.path.join(
                os.getenv(EnvStrings.UPLOAD_FOLDER.value), filename))
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            msg_obj.add_error(MsgArea.UPLOAD_CSV,f"Filetype not supported for {file.filename}")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.getenv(EnvStrings.UPLOAD_FOLDER.value),
                               filename)

@app.route('/', methods=['GET','POST'])
def index():
    upload_file(request)
    msgs = msg_obj.get_all_messages()
    return render_template('index.html',msgs=msgs)


if __name__ == '__main__':
    app_settings = os.getenv(EnvStrings.APP_SETTINGS.value)
    print(f"ENVIRONMENT: {app_settings}")
    app.run()
