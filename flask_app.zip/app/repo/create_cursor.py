from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime
import datetime

db = SQLAlchemy(app)
def connect_db():
    return db

