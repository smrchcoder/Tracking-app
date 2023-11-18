from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from app.repo.create_tables import *  # Assuming Coordinates is a model
from sqlalchemy.exc import SQLAlchemyError  # Import the exception for SQLAlchemy errors
from app.repo.create_tables import *

def insert_route(route_id,name):
    r=route(id=route_id,name=name)
    db=connect_db()
    db.session.add(r)
    db.session.commit()
    return jsonify({'message':"Inserted the routename"})

def route_by_id(id):
    route_obj=route.query.get(id)
    #route_attributes = {"id":route_obj.id,"name":route_obj.name,"intermediate_coordinates":route_obj.intermediate_coordinates,"shuttle_devices":route_obj.shuttle_devices}
    print(route_obj)
    return serialize_route(route_obj)

def serialize_route(route_obj):
    # Check if route_obj is not None before accessing its attributes
    if route_obj:
        intermediate_coordinates = route_obj.intermediate_coordinates
        shuttle_devices = route_obj.shuttle_devices

        return {
            "id": route_obj.id,
            "name": route_obj.name,
            "intermediate_coordinates": [coord.serialize() for coord in intermediate_coordinates] if intermediate_coordinates else [],
            "shuttle_devices": [device.serialize() for device in shuttle_devices] if shuttle_devices else []
            # Add more attributes as needed
        }
    else:
        return {}
