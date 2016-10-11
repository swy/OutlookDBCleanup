#!/usr/bin/python
import shutil
import os.path
import time

now = time.time()
oldenough = now - (30 * 86400)
home = os.path.expanduser("~")
print "Starting in " + home


for dirpath, dirnames, filenames in os.walk (os.path.join(home, "Documents/Microsoft User Data/Office 2011 Identities")):

#Look for 30 day old database files.  I have the "database" part down, not the dual logic.
	for filename in [fname for fname in filenames if "Database" in fname]:
#	
		print "Database found at " + os.path.join(dirpath,filename)

	for dirname in [dname for dname in dirnames if "[Backed up " in dname]:
		print "deleting " + os.path.join(dirpath, dirname)
		#shutil.rmtree(os.path.join(dirpath, dirname))
		