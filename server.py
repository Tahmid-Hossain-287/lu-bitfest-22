from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

class Item(db.Model):
    ID = db.Column(db.String(length=30), unique=True)

@app.route('/')
@app.route('/<path:page_name>')
def hello(page_name="home.html"):
    return render_template({page_name})

@app.route('/regform')
def regform(page_name="regform.html"):
    return render_template({page_name})























# Choose what tools to use. sqlite? session? fix one and then proceed.
# Corey Schafer uses flask_bcrypt, flask_login, flask_sqlalchemy
# tech with tim uses from flask import session, sqlalchemy in his 2019 tutorial.
# jimshpaedcoding uses sqlalchemy, bcrypt. Tutoridal date in 2021, March.
# Jake Rieger from freecodecamp uses SQLAlchemy 