#!/usr/bin/env python

import sys, os, re, codecs
from StringIO import StringIO
from docutils.core import publish_string
from lxml import etree

DIR = os.path.abspath(os.path.dirname(__file__))
DOCUTILS_DTD = os.path.join(DIR, 'lib', 'dtd', 'docutils.dtd')
F_NAMESPACE = etree.FunctionNamespace('http://benglynn.net/rstx')
HTML_NS = 'http://www.w3.org/1999/xhtml'
POST_NAME = 'post.rst'
XSLT_PATH = os.path.join(DIR, 'lib', 'xslt', 'site.xsl')


class Directory(object):
    """ A directory in the hierarchy for which to generate an index html file. """


    class DTDResolver(etree.Resolver):
        """ Resolve the DTD with a filesystem copy to speed up parsing. Subsequent 
        URLs are relative, and so resolve correctly once the first is found."""
        def resolve(self, url, id, context):
            if url == 'http://docutils.sourceforge.net/docs/ref/docutils.dtd':
                return self.resolve_filename(DOCUTILS_DTD, context)
            return None


    parser = etree.XMLParser(dtd_validation=True, remove_blank_text=True)
    parser.resolvers.add(DTDResolver())
    transform = etree.XSLT(etree.parse(XSLT_PATH))


    def __init__(self, dirpath, parent=None):
        self.parent = parent
        self.dirpath = dirpath
        self.dirname = os.path.split(self.dirpath)[-1]
        self.children = []
        self.path = self.parent and '%s%s/' % (self.parent.path, self.dirname) \
            or '/'

        self.root = self
        while self.root.parent:
            self.root = self.root.parent


        # Get reST as XML
        rstfilepath = os.path.join(self.dirpath, POST_NAME)
        rstfile = codecs.open(rstfilepath, encoding='utf-8')
        self.rst = unicode(rstfile.read())
        rstfile.close()
        xmlstring = publish_string(self.rst, writer_name='xml')
        self.xml = etree.parse(StringIO(xmlstring), Directory.parser)

        # Get metadata for this post
        self.title = self.xml.xpath('title/text()')[0]
        # todo: tags, date and other metadat that might be used in navigation

        # Add to the XML site structure
        attributes = {
            'path': self.path,
            'title': self.title,}
        self.element = etree.Element('directory', **attributes)
        if self.parent:
            parent.element.append(self.element)

        # Recurse
        self.find_children()

    def publish(self):
        """ Recursively publish the html for each directory. """

        # Construct the xml for this directory
        rstx = etree.Element('rstx', path=self.path)
        rstx.append(self.root.element)
        rstx.append(self.xml.getroot())
        
        # Write html
        html = Directory.transform(rstx, exampleparam='test')
        prettyhtml = etree.tostring(html, pretty_print=True)
        htmlfile = codecs.open(os.path.join(self.dirpath, 'index.html'), 'w', 
            encoding='utf-8')
        htmlfile.write(prettyhtml)
        htmlfile.close()

        # Write XML whilst designing
        prettyxml = etree.tostring(rstx, pretty_print=True)
        xmlfile = codecs.open(os.path.join(self.dirpath, 'index.xml'), 'w', 
            encoding='utf-8')
        xmlfile.write(prettyxml)
        xmlfile.close()

        # Recurse
        for child in self.children:
            child.publish()


    def find_children(self):
        """ Recursively add Directory instances for all child directories 
        containing post files. """
        # For each item in this directory
        for name in os.listdir(self.dirpath):
            fullpath = os.path.join(self.dirpath, name)
            # If the item's a directory
            if os.path.isdir(fullpath):
                # If the directory has a post
                if os.path.isfile(os.path.join(fullpath, POST_NAME)):
                    self.children.append(Directory(fullpath, self))


# Create a node list of media
# todo: get this into Directory instances?
def media(context):
    media = etree.Element('media')
    js = etree.SubElement(media, 'script', src='/script/main.js')
    css = etree.SubElement(media, 'file')
    return media
F_NAMESPACE['media'] = media

