#!/usr/bin/env python

import sys, os, re, codecs
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

DIR = os.path.abspath(os.path.dirname(__file__))
DOCUTILS_DTD = os.path.join(DIR, 'dtd', 'docutils.dtd')

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

class DTDResolver(etree.Resolver):
    """ Resolve the DTD with a filesystem copy to speed up parsing. Subsequent 
    URLs are relative, and so resolve correctly once the first is found."""
    def resolve(self, url, id, context):
        if url == 'http://docutils.sourceforge.net/docs/ref/docutils.dtd':
            return self.resolve_filename(DOCUTILS_DTD, context)
        return None

parser = etree.XMLParser(dtd_validation=True, remove_blank_text=True)
parser.resolvers.add(DTDResolver())
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

prettyhtml = etree.tostring(transform(tree), pretty_print=True)
htmlfile = codecs.open('index.html', 'w', encoding='utf-8')
htmlfile.write(prettyhtml)
htmlfile.close()

