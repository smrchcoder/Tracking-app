from app import app
from app.services.distance import cal_distance_duration
from flask import request, jsonify
import json
from decimal import Decimal
#given any coordinates tries to find the distance btween them
#used to find the distnace between the current cord and intermediate cord[0] to check if they are at a distnace of <10
@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    try:
        if request.method == 'POST':
            # Use request.form to get parameters from the POST request body
            data = request.form
            current_cord = json.loads(data.get('current_cord'))
            destination_cord = json.loads(data.get('destination_cord'))

        elif request.method == 'GET':
            # Use request.args to get parameters from the URL for GET request
            current_cord = json.loads(request.args.get('current_cord'))
            destination_cord = json.loads(request.args.get('destination_cord'))

        origin_cord = (Decimal(current_cord['latitude']), Decimal(current_cord['longitude']))
        dest_cord = (Decimal(destination_cord['latitude']), Decimal(destination_cord['longitude']))

        result = cal_distance_duration(origin_cord, dest_cord)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
