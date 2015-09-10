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
