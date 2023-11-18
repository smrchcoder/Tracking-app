from app.repo.create_cursor import connect_db
from app.repo.create_tables import *
from flask import Flask, request, jsonify
def services_insert_data(device_id,latitude,longitude):
    try:
        db= connect_db() 
        
        gps=GPS(device_id=device_id,latitude=latitude,longitude=longitude)
        db.session.add(gps)
        db.session.commit()
        existing_device = db.session.query(shuttle_devices).filter_by(device_id=device_id).first()

        if existing_device:
            # Update the initial coordinates
            existing_device.intial_latitude = latitude
            existing_device.intial_longitude = longitude
        else:
            # If the device doesn't exist, create a new record
            new_device = shuttle_devices(device_id=device_id, intial_latitude=latitude, intial_longitude=longitude)
            db.session.add(new_device)

        db.session.commit()
        return jsonify({"message": "Data inserted successfully and Initial coordinates updated"})
    except Exception as e:
        return jsonify({"error": str(e)})