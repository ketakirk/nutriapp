from app.dbops.data_access import *

# Test create_profile
fname = "rohan"
lname = "ketaki"
state = "Hawaii"
pid = create_profile(fname, lname, state)
print("Created profile %s" % pid)

# Test read_profile
print(read_profile(pid))

# Test update_profile
colname = "state"
colval = "Michigan"
pid = "62153a6f-02b3-4e1e-8a40-080c622ed531"
update_profile(pid, colname, colval)
print("updated %s to %s for profile %s"
		% (colname, colval, pid))

# Test delete_profile
pid = "62153a6f-02b3-4e1e-8a40-080c622ed531"
delete_profile(pid)
print("Deleted profile %s" % pid)