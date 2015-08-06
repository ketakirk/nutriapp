import psycopg2 as pg2
import uuid

def execute(stmt):
	# Open connection
	conn = pg2.connect(	database="webapp", 
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

def create_profile(fname, lname, state):
	# Compose query or stmt
	profile_id = str(uuid.uuid4())
	res = execute('''insert into profiles
			  (profile_id, first_name, last_name, state)
			  values ('%s', '%s', '%s', '%s');	
			''' % (profile_id, fname, lname, state)
	)

	# Return the id of the object created
	return profile_id;

def read_profile(pid):
	res = execute("select * from profiles where profile_id = '%s'" % pid)
	return res

def update_profile(pid, columnname, columnval):
	res = execute(
		"update profiles set %s = '%s' where profile_id = '%s';"
			% (columnname, columnval, pid))
	return res

def delete_profile(profile_id):
	res = execute("delete from profiles where profile_id = '%s'"
					% profile_id)
	return res


