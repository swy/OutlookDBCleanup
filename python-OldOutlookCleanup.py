#!/usr/bin/python
import shutil
import os.path

home = os.path.expanduser("~")
print "Starting in " + home

for dirpath, dirnames, filenames in os.walk (home + "/Documents/Microsoft User Data/Office 2011 Identities"):
	for dirname in [f for f in dirnames if "[Backed up " in f]:
		print "deleting " + os.path.join(dirpath, dirname)
		shutil.rmtree(os.path.join(dirpath, dirname))
		