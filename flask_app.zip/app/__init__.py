from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import googlemaps
from flask_login import LoginManager
app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
app.static_folder = 'static'
swaggerui_blueprint=get_swaggerui_blueprint(app.config['SWAGGER_URL'],app.config['API_URL'],config={'app_name':"Tracking Application"})

app.register_blueprint(swaggerui_blueprint)
# for manneging the logged in user the configuration
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from app.routes import insert_data,front_end,userApis,register,set_cordinate,initial_route,dest_route,shuttle_insert,current_cord,get_route,distance_duration,distance_per_device
from app.routes.route import *


