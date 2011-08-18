#!/usr/bin/env python

import sys
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

try:
    filename = sys.argv[1]
except IndexError:
    print 'Usage: %s <filename>' % sys.argv[0]
    sys.exit(1)

# Convert the reST file to xml
file = open(filename, 'r')
rst = unicode(file.read()).encode('utf-8')
xml = publish_string(rst, writer_name='xml')

# Parse the xml
parser = etree.XMLParser(dtd_validation=True, no_network=False)
tree = etree.parse(StringIO(xml), parser)
print etree.tostring(tree.getroot(), pretty_print=True)
