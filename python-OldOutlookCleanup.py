#!/usr/bin/python
import shutil
# use of shutil: shutil.rmtree('/folder_name')
from glob import iglob
import os
import os.path


for dirpath, dirnames, filenames in os.walk ("/Users/syuroff/Documents/Microsoft User Data/Office 2011 Identities"):
	for dirname in [f for f in dirnames if "[Backed up " in f]:
		print os.path.join(dirpath, dirname)
		shutil.rmtree(os.path.join(dirpath, dirname))
		#shutil.rmtree(dirpath, dirname)