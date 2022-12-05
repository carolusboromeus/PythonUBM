from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/kampus')
def getkampus():
    return render_template('Table.html')

@app.route('/login')
def getlogin():
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)