#!/usr/bin/python

import sys
import os

file = sys.argv[1]
fsize = os.path.getsize(file)
print fsize
