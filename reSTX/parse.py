#!/usr/bin/env python

import sys, os, re
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

DTD = 'docutils.dtd'
DIR = os.path.abspath(os.path.dirname(__file__))
DTDDIR = os.path.join(DIR, 'dtd')
DTDURI = 'file://%s/%s' % (DTDDIR, DTD)

try:
    filename = sys.argv[1]
except IndexError:
    print 'Usage: %s <filename>' % sys.argv[0]
    sys.exit(1)

# Convert the reST file to xml
file = open(filename, 'r')
rst = unicode(file.read()).encode('utf-8')
xml = publish_string(rst, writer_name='xml')

# Replace DTD reference to local DTD
pattern = r'"[^"]+%s"' % DTD
xml = re.sub(pattern, '"%s"' % DTDURI, xml)

# Parse the xml
parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse(StringIO(xml), parser)
pretty =  etree.tostring(tree.getroot(), pretty_print=True)

print pretty

