from flask import Flask, request, redirect, url_for, render_template
from flask_restful import Api, Resource, reqparse

from flask_sqlalchemy import SQLAlchemy

from resources.hello_world import HelloWorld
import resources.video as video
import os

app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
    return render_template("base.html")

api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(video.Video, "/video/<int:video_id>")
api.add_resource(video.AllVideos, "/videos")

@app.route("/<name>")
def user(name):
    return render_template("names.html", name=name, all=['Daniel', 'yo', 'yo soy', 'afa'])

@app.route('/new_name')
def new_name():
    return render_template('new_name.html', all=['Daniel', 'yo', 'yo soy', 'afa'] )

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test/repo')
def repo():
    return render_template('index.html')


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'This is the default route'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)