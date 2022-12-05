from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app3 = Flask(__name__)
app3.config['UPLOAD_FOLDER'] = os.path.relpath('.') + \
                               '/static/upload'
app3.config['MAX_CONTENT_PATH'] = 10000000

@app3.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = app3.config['UPLOAD_FOLDER'] + '/' + \
            secure_filename(f.filename)
        try:
            f.save(filename)
            return render_template('upload-sukses.html', \
                   filename=secure_filename(f.filename))
        except:
            return render_template('upload-gagal.html', \
                   filename=secure_filename(f.filename))
    return render_template('form-upload.html')

if __name__ == '__main__':
    app3.run(debug=True)