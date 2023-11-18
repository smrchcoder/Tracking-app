from app import app
from flask import Flask ,jsonify,request
from app.services.getroute import routecord
# depricated don't use use new one from route
@app.route('/getroute',methods=['GET', 'POST'])
def getroute():
    if request.method == 'GET':
        route_id=request.args.get('route_id')
    else:
        route_id=request.form.get('route_id')
    return routecord(route_id)