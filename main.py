from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from hello_world import HelloWorld
import video

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(video.Video, "/video/<int:video_id>")
api.add_resource(video.AllVideos, "/videos")

if __name__ == "__main__":
    app.run(debug=True)