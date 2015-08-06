"""
Generates random profile data by reading files in this dir.
Usage: python generate.py
"""

import uuid
import random
print(__doc__)
# first create lists of first names, last names, and states
fnames = open("fnames.txt").read().splitlines()[:1000]
lnames = open("lnames.txt").read().splitlines()
states = open("states.csv").read().splitlines()

num_profiles = 10000
with open("profiles.csv", "w") as ofh:
	for _ in range(num_profiles):
		rid = uuid.uuid4()
		rfname = fnames[random.randint(0,999)]
		rlname = lnames[random.randint(0,999)]
		rstate = states[random.randint(0,49)].split(",")[0].replace('"', '')
		ofh.write("%s,%s,%s,%s\n"%(rid, rfname, rlname, rstate))


