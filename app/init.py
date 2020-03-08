from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUBJECTTTT2CHA@NGE"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:vampirelove98@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
