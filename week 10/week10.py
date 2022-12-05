from flask import Flask, render_template
import pdfkit
import os

app10 = Flask(__name__)
app10.config['PDF_FOLDER'] = os.path.realpath('.') + '/static/pdf'
app10.config['TEMPLATE_FOLDER'] = os.path.realpath('.') + '/templates'
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app10.route('/')
def index():
    return render_template('index.html')

@app10.route('/konversi')
def konversi():
    htmlfile = app10.config['TEMPLATE_FOLDER'] + '/index.html'
    pdffile = app10.config['PDF_FOLDER'] + '/demo4.pdf'
    pdfkit.from_file(htmlfile, pdffile, configuration=config)
    return '''
        Proses konversi ke PDF telah berhasil. <br/>
        Klik <a href="http://localhost:5000/static/pdf/demo4.pdf">di sini</a>
        untuk membuka file tersebut.
        '''
if __name__=='__main__':
    app10.run(debug=True)