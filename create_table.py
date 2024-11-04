# create_tables.py
from main import app
  # Import the app and db from your main.py
from db import db

# Import your models here to ensure they are registered with the db
from models import *  # Adjust the import based on your project structure

with app.app_context():
    print("Creating all tables...")
    db.create_all()
    print("Tables created!")
