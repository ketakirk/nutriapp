import psycopg2 as pg2
import uuid

def execute(stmt):
	"""
	A utility function used by create- , read-, update- and delete-.
	Executes input SQL statement 'stmt' and returns query results 
	if any. 
	:param stmt: SQL statement to execute
	"""
	# Open connection
	conn = pg2.connect(	database="nutriapp", 
						user="rohan")

	# Create cursor
	curs = conn.cursor()

	# Execute qry or stmt and commit (finalize) the transaction
	curs.execute(stmt)
	conn.commit()

	# Capture result
	try:
		result = curs.fetchall()
	except pg2.ProgrammingError:
		# No results to fetch
		result = None

	# Close cursor
	curs.close()

	# Close connection
	conn.close()

	return result

def create_profile(food_code, display_name, portion_default, portion_amt, solid_fats, added_sugars, calories, saturated_fats):
	"""
	---
	:param food_code:
	:param display_name:
	:param portion_default:
	:param portion_amt:
	:param solid_fats:
	:param added_sugars:
	:param calories:
	:param saturated_fats:
	:return: 
	"""
	# Compose query or stmt
	food_id = str(uuid.uuid4())
	res = execute('''insert into profiles
			  (food_id, food_code, display_name, portion_default, portion_amt, solid_fats, added_sugars, calories, saturated_fats)
			  values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');	
			''' % (food_id, food_code, display_name, portion_default, portion_amt, solid_fats, added_sugars, calories, saturated_fats)
	)

	# Return the id of the object created
	return food_id;

def read_profile(fid):
	res = execute("select * from profiles where food_id = '%s'" % fid)
	return res

def update_profile(fid, columnname, columnval):
	res = execute(
		"update profiles set %s = '%s' where food_id = '%s';"
			% (columnname, columnval, fid))
	return res

if __name__ == "__main__":

	print("Testing execute()")
	qry = "select count (*) from profiles;"
	res = execute(qry)
	assert res[0][0] == 2014

	print("Testing read()")
	res = read_profile('8005f212-544b-4715-86e9-035bace34071')
	assert res[0][2] == 'Ice cream, regular'

	print('Tests passed')



	