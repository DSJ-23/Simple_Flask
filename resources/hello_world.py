from flask import Flask
from flask_restful import Api, Resource

class HelloWorld(Resource):
    def get(self, name):
        return {"data": name}

    def post(self):
        return {"data": "Posted"}