#!/usr/bin/python

from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import glob, os, shutil

try:
    current_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
except TypeError:
    nouser = 'No user logged in.'
    raise Exception(nouser)

documents_path = "/Users/" + current_user + "/Documents/Microsoft User Data/Office 2011 Identities"

current_database = max(glob.iglob(documents_path + '/*Identity*/Database'), key=os.path.getmtime)

print "Current database (based on most recently modified path) is " + current_database

for d in glob.iglob(documents_path + '/*Identity*/Database'):
    if d == current_database:
        continue
    else:
        pd = d.rstrip('Database')
      #  shutil.rmtree(pd)
      	print "script will remove " + pd