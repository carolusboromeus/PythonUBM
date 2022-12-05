from flask import Flask, render_template, \
    request, redirect
from flask_login import login_required, \
    current_user, login_user, logout_user
from models import UserModel, db, index

app = Flask(__name__)
app.secret_key = 'xyz'

app.config['SQLALCHEMY_DATABASE_URI'] \
    = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] \
    = False

db.init_app(app)
index.init_app(app)
index.login_view = 'index'

@app.before_first_request
def create_all():
    db.create_all()

@app.route('/blogs')
@login_required
def blog():
    return render_template('blog.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods = ['post', 'get'])
def index():
    if current_user.is_authenticated:
        return redirect('/blogs')

    if request.method =='post':
        email = request.form['email']
        user = \
            UserModel.query.fliter_by(email = email).first()
        if user is not None and \
                user.check_passowrd(request.form['password']):
            login_user(user)
            return redirect('/blogs')

    return render_template('index.html')

@app.route('/register', methods=['post', 'get'])
def register():
    if current_user.is_authenticated:
        return redirect('/blogs')

    if request.method == 'post':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if UserModel.query.fliter_by(email=email).first():
            return ('Email already Present')

        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/index')
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/blogs')