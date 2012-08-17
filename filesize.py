#!/usr/bin/python

import sys
import os

filepath = sys.argv[1]
fsize = os.path.getsize(filepath)
print fsize
