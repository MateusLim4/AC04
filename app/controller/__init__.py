from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aluno.db'
db = SQLAlchemy(app)

from app.controller import default


