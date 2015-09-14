import json
from ..dbops import data_access as db

def read_profile(fid):
    """
    Calls the db module to read profile data 
    directly from database. Creates JSON response
    from raw database response and returns
    """

    # Call the db module and retrieve the row 
    # corresponding to food_id. At this point
    # retval is simply a list of tuples
    # Example: retval = [('e1bfebfc-91fb-4fa3-b90c-f618b59a8b67', '12350000', 'Sour cream dip', '1.00000', '.25000', '105.64850', '1.57001', '133.65000', '7.36898')]
    retval = db.read_profile(fid)

    # Construct a JSON from raw database list of tuples.
    # If data for given fid was not found, return empty
    if retval:
        profile = { "status": "ok",
                    "food_data": {
                        "food_id": retval[0][0],
                        "food_code": retval[0][1],
                        "display_name": retval[0][2],
                        "portion_default": retval[0][3],
                        "portion_amt": retval[0][4],
                        "solid_fats": retval[0][5],
                        "added_sugars": retval[0][6],
                        "calories": retval[0][7],
                        "saturated_fats": retval[0][8],
                    }
                }
    else:
        profile = {"status": "fail", "food_data": "not found"}

    # Convert 'profile' dictionary to JSON using json.dumps
    return json.dumps(profile)


def get_food_betw_cal(mincal, maxcal):

    retval = db.get_food_betw_cal(mincal, maxcal)

    fil = []
    for t in retval:
        fil.append(
            {"display_name": t[2], 
            "calories": t[7]}
            )
    # print(fil)

    if retval:

            food_betw_cal = { "status": "ok",
                            "food_data": fil
                        }
            
    else:
        food_betw_cal = {"status": "fail", "food_data": "not found"}

    print(food_betw_cal)
    return json.dumps(food_betw_cal)

if __name__ == '__main__':
    get_food_betw_cal(100, 200)





