import json
from ..dbops import data_access as db

def read_profile(pid):
    """
    Calls the db module to read profile data 
    directly from database. Creates JSON response
    from raw database response and returns
    """

    # Call the db module and retrieve the row 
    # corresponding to profile_id. At this point
    # retval is simply a list of tuples
    # Example: retval = [('b184384c-856c-4882-b146-c142ed353996', 'rohan', 'ketaki', 'Hawaii')]
    retval = db.read_profile(pid)

    # Construct a JSON from raw database list of tuples.
    # If data for given pid was not found, return empty
    if retval:
        profile = { "status": "ok",
                    "profile_data": {
                        "profile_id": retval[0][0],
                        "first_name": retval[0][1],
                        "last_name": retval[0][2],
                        "state": retval[0][3]
                    }
                }
    else:
        profile = {"status": "fail", "profile_data": "not found"}

    # Convert 'profile' dictionary to JSON using json.dumps
    return json.dumps(profile)

def create_profile(fname, lname, state):
    pid = db.create_profile(fname, lname, state)
    response = {
        "status": "ok",
        "profile_id": pid
    }

    return json.dumps(response)

def update_profile(pid, colkey, colval):
    db.update_profile(pid, colkey, colval)
    retval = {
        "status": "ok",
        "profile_id": pid
    }
    return json.dumps(retval)





