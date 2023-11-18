from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from app.services.initial import initial
#for now this is not needed sir
@app.route('/initial_cord',methods=['GET', 'POST'])
def initial_cord():
    if request.method == 'POST':
        route_id=request.form.get('route_id')
    else:
        route_id=request.args.get('route_id')
    return initial(route_id)
