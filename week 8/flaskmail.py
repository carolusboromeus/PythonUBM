from flask import Flask, render_template, request
from flask_mail import Mail, Message

app2 = Flask(__name__)
app2.config['MAIL_SERVER'] = 'smtp.gmail.com'
app2.config['MAIL_PORT'] = 465
app2.config['MAIL_USE_TLS'] = False
app2.config['MAIL_USE_SSL'] = True

@app2.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form['txtUserName']
        password = request.form['txtPassword']
        to = request.form['txtTo']
        subject = request.form['txtSubject']
        message = request.form['areaMessage']

        app2.config['MAIL_USERNAME'] = username
        app2.config['MAIL_PASSWORD'] = password

        pesan = Message(subject, sender=username, recipients=[to])
        pesan.body = message

        mail = Mail(app2)
        mail.connect()
        mail.send(pesan)
        return render_template('sukses.html', to=to)

        # try:

        # except:
        #     return render_template('gagal.html')
    return render_template('form.html')

if __name__ == '__main__':
    app2.run(debug=True)