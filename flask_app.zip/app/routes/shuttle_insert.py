from app import app
from flask import Flask, request, jsonify
from app.services.initial import initial
from app.services.destination import destination
from app.services.shuttle_insert import insert_shuttle_s,shuttle_to_route
@app.route('/insert_shuttle',methods=['POST','GET'])
def insert_shuttle():
    if request.method == 'POST':
        device_id=request.form.get('device_id')
        route_id=request.form.get('route_id')
    else:
        device_id=request.args.get('device_id')
        route_id=request.args.get('route_id')
    Cord_intital=initial(route_id)
    #Cord_destination=destination(route_id)

    return insert_shuttle_s(device_id,Cord_intital["latitude"],Cord_intital['longitude'],route_id)

@app.route('/shuttel', methods=['POST'])
def assign_route_to_shttle():
    print('in request')
    data = request.get_json()

    device_id = int(data['shuttle_id'])
    name = str(data['name'])

    # Check if 'route_id' is present in the data
    if 'route_id' in data:
        route_id = int(data['route_id'])
        print(device_id, name, route_id)
        insert_shuttle_s(device_id, name)
        return shuttle_to_route(device_id, route_id)