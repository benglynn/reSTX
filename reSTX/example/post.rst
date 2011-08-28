===============
An example post
===============

:Author: benglynn
:Date: 2010-08-17
:Tags: javascript, html, css


This is an example of a single post writen in ReST
--------------------------------------------------

Next steps, are to look at the parsing of a file like this, or a directory of
files. Not with the command-line tools in the ``docutils`` package, but with our
own parser. It would then construct a flat site, with everything bound together
with our own navigation. Surely using django templates? But maybe not, maybe
using ``xslt``.

Here's a paragraph. In the document I make sure to keep it's line length below
80 characters, as that'll be our standard.

A list of stuff:

- A simple way to show off the RsT formatting

- Bulleted lists

- A list of stuff

Here's an example of some ``html`` code:

::

  <html>
    <head>
      <title>The title</title>
    </head>
  </html>

And maybe some ``javascript`` code too, indented with just two spaces:

::

  function doSomething (x, y) {
    return x*y;
  }

Okay, that'e enough now! Oh no, hang on, how about a `link to something`_. 
There! Now we're done!

.. _`link to something`: http://www.bbc.co.uk/



