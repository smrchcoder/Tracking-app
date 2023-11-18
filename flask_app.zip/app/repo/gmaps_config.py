from app import app
import googlemaps
def gmaps_config():
    gmaps = googlemaps.Client(key=app.config['API_KEY'])
    return gmaps