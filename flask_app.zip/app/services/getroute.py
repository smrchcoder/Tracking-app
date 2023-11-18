# Assuming 'coordinates' is defined as a model using SQLAlchemy
from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
# Import your model
# depricated don't use
def routecord(route_id):
    try:
        # Create a database connection
        db = connect_db()

        # Initialize the model without passing the database connection
        cord = coordinates.query  # Assuming Coordinates is your model class

        # Query the database for all rows with the given route_id and order them by the order number
        rows = cord.filter_by(route_id=route_id).order_by(coordinates.order).all()

        # Close the database connection
        #db.close()
        #print("rows", rows)

        # Create a list of lists where each inner list contains [lat, lng]
        result = []
        for row in rows:
            result.append({'lat':row.latitude, 'lng':row.longitude})

        return jsonify(result)

    except Exception as e:
        # Handle exceptions, log errors, etc.
        #print("error")
        return jsonify({'error': str(e)})
