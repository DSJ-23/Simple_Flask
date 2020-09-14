from flask_restful import Api, Resource, reqparse, abort
import random

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video")
video_put_args.add_argument("likes", type=int, help="Likes of the Video")

videos = {
          1: {"name": "Moneyball", "views": 20, "likes": 10},
          2: {"Title": "The Big Short", "views": 20, "likes": 10}
        }

def abort(video_id):
    if video_id in videos:
        abort(409, "Video already exsists")

class Video(Resource):
    def get(self, video_id=0):
        if video_id != 0:
            return videos[video_id]
        else: 
            return videos
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {video_id: args}, 201

    def delete(self, video_id):
        del videos[video_id]
        return '', 204

class AllVideos(Resource):
    def get(self): 
        return videos

    def post(self):
        random_integer = generate_random_integer()
        args = video_put_args.parse_args()
        videos[random_integer] = args
        return {random_integer: args}, 201


def generate_random_integer():
    number = random.randint(1,100)
    if number not in videos:
        return number
    else:
        return generate_random_integer()



