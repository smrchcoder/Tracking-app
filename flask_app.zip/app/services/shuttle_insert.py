from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
def insert_shuttle_s(device_id, shuttle_name):
    db = connect_db()

    # Check if a row with the given device_id and shuttel_name already exists
    existing_shuttle = db.session.query(shuttle_devices).filter_by(device_id=device_id, shuttel_name=shuttle_name).first()

    # If the row doesn't exist, insert a new one
    if existing_shuttle is None:
        shuttle = shuttle_devices(device_id=device_id, shuttel_name=shuttle_name)
        db.session.add(shuttle)
        db.session.commit()
    else:
        print("Row already exists. Not inserting a new one.")

   # return{"message":"Successfully assigned route to the device"}

def shuttle_to_route(device_id,route_id):
    shuttle=shuttle_devices.query.get(device_id)
    current_route=route.query.get(route_id)
    if(shuttle is None or current_route is None):
        return "wrong info"
    shuttle.route_id=route_id
    db.session.add(shuttle)
    db.session.commit()
    return "updated sucessfully"
