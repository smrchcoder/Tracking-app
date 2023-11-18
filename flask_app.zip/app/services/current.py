from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from decimal import Decimal
def current(device_id):
    db=connect_db()
    data=db.session.query(shuttle_devices).filter_by(device_id=device_id).first()
    if data:
        response_data={'latitude':float(data.intial_latitude), 'longitude':float(data.intial_longitude)}
        return jsonify(response_data)
    else:
        return jsonify({"message":"No device Found"})