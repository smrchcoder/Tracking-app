from app import app
from flask import Flask, request, jsonify, render_template
from app.repo.create_cursor import connect_db
from app.services.services_route import insert_route, route_by_id

# this api will create the route object with no shuttels and co-ordinates
@app.route("/createroute", methods=['POST','GET'])
def createroute():
    if request.method == 'POST':
        route_id=request.form.get('id')
        route_name=request.form.get('name')
    else:
        route_id=request.args.get('id')
        route_name=request.args.get('name')
    return insert_route(route_id, route_name)

# this api is to get route using route id
# the route will be consisting of data of all the shuttels associated with it and all the co-ordinates
@app.route("/route/<int:id>")
def get_route_by_id(id):
    return route_by_id(id)