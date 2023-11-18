from flask import Flask
from flask_restful import Api, Resource, reqparse,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///database.db'
db=SQLAlchemy(app)
#creating a tabl with  the bewlow columns
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    views = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"
db.create_all()



# Creating a request parser
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, required=True, help="name of the video")
video_put_args.add_argument("views", type=int, required=True, help="views of the video")
video_put_args.add_argument("likes", type=int, required=True, help="Likes of the video")

videos = {}
def abort_if_video_not_found(video_id):
    if video_id not in videos:
        abort(404)
def abort_if_video_exists(video_id):
     if video_id in videos:
        abort(409,"Video already exists")

class Video(Resource):
    def get(self, video_id):
        if video_id in videos:#could use the abort_if_video_not_found method instead
            return videos[video_id]
        else:
            return {"error": "Video not found"}, 404

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {video_id: args},201#created 
    def delete(self, video_id):
        abort_if_video_not_found(video_id)
        del videos[video_id]
        return {"message": "Video deleted"}, 204#204 stands for deleted sucessfully


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
   
    app.run(debug=True)
