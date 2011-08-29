#!/usr/bin/env python

import sys, os, re, codecs
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

DIR = os.path.abspath(os.path.dirname(__file__))
DOCUTILS_DTD = os.path.join(DIR, 'lib', 'dtd', 'docutils.dtd')
FUNCTION_NS = 'http://benglynn.net/rstx'
HTML_NS = 'http://www.w3.org/1999/xhtml'
EXAMPLE_DIR = os.path.join(DIR, 'example')
POST_NAME = 'post.rst'


class Directory(object):
    """ A directory in the hierarchy for which to generate an index html file.
    This may be the root, or any node or leaf underneath. """
    def __init__(self, dirname, parent=None):
        print dirname
        self.parent = parent
        self.dirname = dirname
        self.children = []
        self.find_children()

    def find_children(self):
        """ Recursively add Directory instances for all child directories 
        containing post files. """
        # For each item in this directory
        for name in os.listdir(self.dirname):
            fullpath = os.path.join(self.dirname, name)
            # If the item's a directory
            if os.path.isdir(fullpath):
                # If the directory has a post
                if os.path.isfile(os.path.join(fullpath, POST_NAME)):
                    self.children.append(Directory(fullpath, self))




# Convert the reST file to xml
file = open(os.path.join(EXAMPLE_DIR, POST_NAME), 'r')
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

# Create a node list of media
def media(context):
    media = etree.Element('media')
    js = etree.SubElement(media, 'script', src='/script/main.js')
    css = etree.SubElement(media, 'file')
    return media
ns = etree.FunctionNamespace(FUNCTION_NS)
ns['media'] = media

# Transform to html
xslname = 'site.xsl'
xsl = etree.parse(os.path.join(DIR, 'lib', 'xslt', xslname))
transform = etree.XSLT(xsl)
html = transform(tree, test='"hello"')
prettyhtml = etree.tostring(html, pretty_print=True)


# Write the html index file
htmlfile = codecs.open(os.path.join(EXAMPLE_DIR, 'index.html'), 'w', 
    encoding='utf-8')
htmlfile.write(prettyhtml)
htmlfile.close()

