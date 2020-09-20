from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from flask_sqlalchemy import SQLAlchemy

from resources.hello_world import HelloWorld
import resources.video as video

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)


api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(video.Video, "/video/<int:video_id>")
api.add_resource(video.AllVideos, "/videos")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)