from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from app.services.destination import destination
#for now this is not needed sir
@app.route('/destination_cord',methods=['GET','POSt'])
def destination_cord():
    if request.method == 'POST':
        route_id=request.form.get('route_id')
    else:
        route_id=request.args.get('route_id')
    
    return destination(route_id)