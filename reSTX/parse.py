#!/usr/bin/env python

import sys, os, re
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

DIR = os.path.abspath(os.path.dirname(__file__))

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
dtdname = 'docutils.dtd'
dtddir = os.path.join(DIR, 'dtd')
dtduri = 'file://%s/%s' % (dtddir, dtdname)
pattern = r'"[^"]+%s"' % dtdname
xml = re.sub(pattern, '"%s"' % dtduri, xml)

# Parse the xml
parser = etree.XMLParser(dtd_validation=True, ns_clean=True, 
    remove_blank_text=True)
tree = etree.parse(StringIO(xml), parser)
pretty =  etree.tostring(tree, pretty_print=True)
# Write the xml to a reference whilst developing
xmlfile = open('xml.xml', 'w')
xmlfile.write(pretty)
xmlfile.close()

# Transform to html
xslname = 'site.xsl'
xsl = etree.parse(os.path.join(DIR, 'xslt', xslname))
transform = etree.XSLT(xsl)

html =  transform(tree)
prettyhtml = etree.tostring(html.getroot(), pretty_print=True)
htmlfile = open('index.html', 'w')
htmlfile.write(prettyhtml)
htmlfile.close()

