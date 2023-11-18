from app.services.services_insert_data import services_insert_data
from app import app
from flask import Flask, request, jsonify
#insert the current cordinates 
from decimal import Decimal
@app.route('/live/cordinates', methods=['GET','POST'])
def insert_data():
    try:
        if request.method == 'POST':
            device_id = request.form.get('device_id')  
            longitude = Decimal(request.form.get('longitude'))
            latitude = Decimal(request.form.get('latitude'))
            
        else:
            device_id = request.args.get('device_id')
            longitude =Decimal(request.args.get('longitude'))
            latitude = Decimal(request.args.get('latitude'))
        
        return services_insert_data(device_id,latitude,longitude)
    except Exception as e:
        print("Error inserting device")
        return jsonify({"error": str(e)})