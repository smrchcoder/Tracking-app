from app import app
from app.repo.create_tables import *
from app.repo.create_cursor import connect_db
from flask import Flask, request, jsonify
from app.services.current import current
#this api is to get the current cordinate of a device_id
@app.route('/current_cord', methods=['GET','POST'])
def current_cord():
    if request.method == 'POST':
        device_id=request.form.get('device_id')
    else:
        device_id=request.args.get('device_id')

    return current(device_id)