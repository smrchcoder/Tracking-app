from app import app
from decimal import Decimal

from flask import Flask, request, jsonify
from app.services.cord_services import cord_insert
@app.route('/coordinate',methods=['GET', 'POST'])
#this api to store all the list of coordinate in any route .
def coordinate():
    data = request.get_json()
    route_id=str(data['device_id'])
    initial_lat =Decimal( data['ilat'])
    initial_lng = Decimal(data['ilng'])
    destination_lat = Decimal(data['dlat'])
    destination_lng = Decimal(data['dlng'])
    cord_list=data['intermidate_cord']
    route_name=data['name']
    sucess=False
    msg=''
    result=cord_insert(route_id, route_name,initial_lat, initial_lng, destination_lat, destination_lng,cord_list)
    if(result==True):
        sucess=True
        msg="Coordinates have been successfully inserted"
    else:
        msg=result
    response_data={'sucess':sucess,'message':msg}
    return jsonify(response_data)