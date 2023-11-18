# Create tables if they don't exist
from .create_cursor import connect_db
from app import app,login_manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime
import datetime
from flask_login import UserMixin


#this is to start login maneger
@login_manager.user_loader
def load_user(user_id):
    return user_table.query.get(int(user_id))

db = connect_db()

class GPS(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    device_id=db.Column(db.Integer)
    timeStamp=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    longitude=db.Column(db.DECIMAL(precision=20, scale=10))
    latitude=db.Column(db.DECIMAL(precision=20, scale=10))



class Display(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255)) 
    route_id=route_id = db.Column(db.Integer, db.ForeignKey('route.id'))

class route(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255)) 
    intermediate_coordinates = db.relationship('coordinates', backref='route')
    shuttle_devices = db.relationship('shuttle_devices', backref='route')


class coordinates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255),default="intermidiate coordinates")
    #device_id = db.Column(db.Integer)
    timeStamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    longitude = db.Column(db.DECIMAL(precision=20, scale=10))
    latitude = db.Column(db.DECIMAL(precision=20, scale=10))
    order=db.Column(db.Integer)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "timeStamp": self.timeStamp.isoformat(),
            "longitude": float(self.longitude),
            "latitude": float(self.latitude),
            "order": self.order,
        }


# added one more feild to confirm user is active
class user_table(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)) 
    email = db.Column(db.String(255))  
    password = db.Column(db.String(255)) 
    is_active = db.Column(db.Boolean, default=True)


class shuttle_devices(db.Model):
    device_id=db.Column(db.Integer, primary_key=True)
    shuttel_name=db.Column(db.String(255)) 
    intial_latitude =db.Column(db.DECIMAL(precision=20, scale=10))
    intial_longitude =db.Column(db.DECIMAL(precision=20, scale=10))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    def serialize(self):
        return {
            "device_id": self.device_id,
            "shuttel_name": self.shuttel_name,
            "intial_latitude": float(self.intial_latitude),
            "intial_longitude": float(self.intial_longitude),
        }


def create_tables_if_not_exist():
    with app.app_context():
        db.create_all()

def encoprate_dbChanges():
    with app.app_context():
        db.drop_all()
        db.create_all()
    