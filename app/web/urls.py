import json
from flask import Response
from flask import request
from .. import webapp
from . import views


# Home page
@webapp.route("/")
def home():
	# retval = json.dumps({"status": "ok", 
	# 					"msg": "This is the front page"})
	# return Response(retval, mimetype="text/json")
	print(request.user_agent)
	return webapp.send_static_file('index.html')



# Read or Update a profile with a profile_id
@webapp.route("/profile/<profile_id>", methods=["GET", "PUT", "DELETE"])
def read_profile(profile_id):
	# Extract column name and columns value to modify
	colkey = request.args.get("key")
	colval = request.args.get("value")

	if (colkey is None)	and (colval is None):
		profile = views.read_profile(profile_id)
		return Response(profile, mimetype="text/json")
	else:
		resp = views.update_profile(profile_id, colkey, colval)
		updated_profile = views.read_profile(profile_id)
		return Response(updated_profile, mimetype="text/json")

# Create a new profile with fname, lname and state
@webapp.route("/profile", methods=["POST"])
def create_profile():
	# Extract URL paramaters from request
	fname = request.args.get("fname", " ")
	lname = request.args.get("lname", " ")
	state = request.args.get("state", " ")
	resp = views.create_profile(fname, lname, state)
	return Response(resp, mimetype="text/json")
