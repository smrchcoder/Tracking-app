import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCN5ri2E7xT1WLK1C_S1PHjnurHmclw7zM')

def cal_distance_duration(origin_coords,destination_coords):
            
     
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

            #print("for this cordinate",origin_coords,destination_coords)
            #print(distance_in_kilometers,duration_in_minutes)
            return {"distance": distance_in_kilometers, "duration": duration_in_minutes}
            