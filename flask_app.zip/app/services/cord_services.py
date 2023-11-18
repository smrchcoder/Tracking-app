from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from app.repo.create_tables import * # Assuming Coordinates is a model
from sqlalchemy.exc import SQLAlchemyError  # Import the exception for SQLAlchemy errors

def cord_insert(route_id, route_name,ilat, ilng, dlat, dlng, cord_list):
    try:
        cord = []  # List of all the intermediate coordinates
        cord.append([ilat, ilng])

        for i in cord_list:
            temp = i.split(',')
            x = [float(temp[0]), float(temp[1])]
            cord.append(x)

        cord.append([dlat, dlng])

        db = connect_db()  # Assuming this establishes a database connection
        existing_route = route.query.filter_by(id=route_id).first()

        if not existing_route:
            # Create a new route if it doesn't exist
            new_route = route(id=route_id, name=route_name)
            db.session.add(new_route)
        # Delete previous data for the given route_id
        db.session.query(coordinates).filter_by(route_id=route_id).delete()

        for i in range(len(cord)):
            print(cord[i])
            coordinate = coordinates(name="coord" + str(i), longitude=cord[i][1], latitude=cord[i][0], order=i, route_id=route_id)
            db.session.add(coordinate)

        db.session.commit()

        return True
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back the transaction in case of an error
        return str(e)  # You can return the exception message or handle it as needed
