from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
#getting the intial cordinate of any route based on its route_id
def initial(route_id):
    db=connect_db()
    query = db.session.query(coordinates).filter(
coordinates.route_id == route_id,
    coordinates.order == db.session.query(func.min(coordinates.order)).filter(
        coordinates.route_id ==route_id
    )
)

    result = query.first()  
    if result:
        lng=result.longitude
        lat=result.latitude
        response_data={'latitude':lat,'longitude':lng}
        return response_data
    return jsonify({"latitude":-1,'longitude':-1})