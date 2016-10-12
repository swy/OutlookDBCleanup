
#!/usr/bin/python

from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import glob, os, shutil

try:
    current_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
except TypeError:
    nouser = 'No user logged in.'
    raise Exception(nouser)

documents_path = "/Users/" + current_user + "/Documents/Microsoft User Data/Office 2011 Identities"
current_identity = max(glob.iglob(documents_path + '/*Identity*'), key=os.path.getmtime)

for f in glob.iglob(documents_path + "/*"):
    if f != current_identity:
        shutil.rmtree(f)
