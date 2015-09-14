import json
from flask import Response
from flask import request
from .. import nutriapp
from . import views


# Home page
@nutriapp.route("/", methods=["GET"])
def home():
    return nutriapp.send_static_file('index.html')

# Read a profile with a profile_id
@nutriapp.route("/profile/<fid>", methods=["GET"])
def read_profile(fid):    
    profile = views.read_profile(fid)
    return Response(profile, mimetype="text/json")

# Read profiles between minimum and maximum calories
@nutriapp.route("/between", methods=["GET"])
def get_food_betw_cal():
	# Extract URL parameters from request
	mincal = request.args.get("mincal", " ")
	maxcal = request.args.get("maxcal", " ")
	# print(mincal, maxcal)
	food_betw_cal = views.get_food_betw_cal(mincal, maxcal)
	return Response(food_betw_cal, mimetype="text/json")
