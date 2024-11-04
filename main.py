from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
from db import db 

from models import *

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/ecommerce'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

# @app._got_first_request-
# def create_tablesss():
#     db.create_all()  # Create tables

# Import views at the end to avoid circular imports
from views import *
from admin import *

if __name__ == '__main__':
    app.run(debug=True)
