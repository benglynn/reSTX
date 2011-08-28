#!/usr/bin/env python

import os

DIR =  os.path.abspath(os.path.dirname(__file__))

from reSTX.parse import Directory
root = Directory(DIR)
print root.publish()


