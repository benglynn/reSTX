#!/usr/bin/env python

import sys
from docutils.core import publish_string
import lxml

try:
    filename = sys.argv[1]
except IndexError:
    print 'Usage: %s <filename>' % sys.argv[0]
    sys.exit(1)

file = open(filename, 'r')
rst = unicode(file.read()).encode('utf-8')
xml = publish_string(rst, writer_name='xml')

print xml
