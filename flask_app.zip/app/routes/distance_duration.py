from flask import Flask, request, jsonify

import googlemaps
from app import app
from app.services.distance import cal_distance_duration
import json
from decimal import Decimal
# Initialize the Google Maps client with your API key.
gmaps = googlemaps.Client(key='AIzaSyCN5ri2E7xT1WLK1C_S1PHjnurHmclw7zM')
#return the distance :given current_cord,destination_cord and intermidate cord
@app.route('/duration/distance', methods=['POST', 'GET'])
def calculate_distance_and_duration():
    try:
        if request.method == 'POST':
            # Use request.json to get parameters from the POST request body
            data = request.get_json()
            print(data)
            current_cord = data.get('current_cord')
            initial_cord = current_cord
            destination_cord = data.get('destination_cord')
            waypoints = data.get('intermediate_cord')
        elif request.method == 'GET':
            # Use request.args to get parameters from the URL for GET request
            current_cord = json.loads(request.args.get('current_cord'))
            initial_cord = current_cord
            destination_cord = json.loads(request.args.get('destination_cord'))
            waypoints = json.loads(request.args.get('intermediate_cord'))

        total_distance = 0
        total_duration = 0
        if waypoints!=[]:
            origin_cord = (Decimal(initial_cord['latitude']), Decimal(initial_cord['longitude']))
            dest_cord = (Decimal(waypoints[0]['latitude']), Decimal(waypoints[0]['longitude']))
        # print("tuple code", origin_cord, dest_cord)
            temp = cal_distance_duration(origin_cord, dest_cord)
        # print(temp)
            total_distance += temp['distance']
            total_duration += temp['duration']
            waypoints.append(destination_cord)
            for i in range(len(waypoints) - 1):
                x1 = (Decimal(waypoints[i]['latitude']), Decimal(waypoints[i]['longitude']))
                x2 = (Decimal(waypoints[i + 1]['latitude']), Decimal(waypoints[i + 1]['longitude']))
                temp1 = cal_distance_duration(x1, x2)
                total_distance += temp1['distance']
                total_duration += temp1['duration']
        else:
            x1=(Decimal(initial_cord['latitude']), Decimal(initial_cord['longitude']))
            x2=(Decimal(destination_cord['latitude']), Decimal(destination_cord['longitude']))
            temp1 = cal_distance_duration(x1, x2)
            total_distance += temp1['distance']
            total_duration += temp1['duration']
        print("For this cordinates:",initial_cord,destination_cord,waypoints)
        print("The distance achieved is ",total_distance,total_duration)
        return {'distance': total_distance, 'duration': total_duration}

    except Exception as e:
        return jsonify({'error': str(e)}), 500
