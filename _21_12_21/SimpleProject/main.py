from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLAlchemy_DATABASE_URI']='sqllite:///database.db'
app.config['Secretkey']='thisisverysecret'


class User(db):
    id=db.Column(db.String(length=30),nullable=False,primary_key=True)
    username=db.Column(db.String(length=20),nullable=False)
    password=db.Column(db.String(length=20),nullable=False)


@app.route('/')
def home_page():
   return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True,port=9002)