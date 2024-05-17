from flask import *

from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5d7f8e99578556d1dcb8c208593b7550'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes

