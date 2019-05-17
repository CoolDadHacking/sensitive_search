#!/usr/bin/python

# cooldadhacking 2019
# Quick script uses a regular expresion to recursively search a network drive for sensitive info.
# This script was used to look for HIPAA violations in databases.

import os
import re


rootdir=('D:\\')
for folder, dirs, files in os.walk(rootdir):
	try:
		for file in files:
			fullpath = os.path.join(folder, file)
			with open(fullpath, 'r') as f:
				for line in f:
					if re.search(r"(?<!\d)\d{9}(?!\d)", line) is not None:
						print(fullpath)
						break
	except:
		pass

# todo regex for xxx-xx-xxxx
# license, passports, images
# usernames and passwords
