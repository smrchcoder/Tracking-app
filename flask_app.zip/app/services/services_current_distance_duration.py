from app.repo.create_cursor import connect_db
from flask import  jsonify
from app.repo.gmaps_config import gmaps_config
def services_current_distance_duration(lat,lng,dlat,dlng):
    try:
           # Use the distance_matrix function to calculate the distance and duration
            lat=float(lat)
            lng=float(lng)
            dlat=float(dlat)
            dlng=float(dlng)
            origin_coords = (lat, lng)
            destination_coords = (dlat, dlng)
            gmaps=gmaps_config()
            matrix = gmaps.distance_matrix(
                origin_coords, destination_coords, units="metric", mode="driving"
            )
            
            #print(matrix)
            # Extract the distance value (in meters) from the response
            distance_in_meters = matrix["rows"][0]["elements"][0]["distance"]["value"]

            # Extract the duration value (in seconds) from the response
            duration_in_seconds = matrix["rows"][0]["elements"][0]["duration"]["value"]

            # Convert meters to kilometers
            distance_in_kilometers = distance_in_meters / 1000

            # Convert seconds to minutes
            duration_in_minutes = duration_in_seconds / 60

            #print(distance_in_kilometers,duration_in_minutes)
            return {"distance": distance_in_kilometers, "duration": duration_in_minutes}

    except Exception as e:
        #return jsonify({"error": "An error occurred while calculating distance and duration"})
        #print("error")
        return jsonify({"error": str(e)})




