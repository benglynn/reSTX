<xsl:stylesheet 
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rstx="http://benglynn.net/rstx"
  xmlns:html="http://www.w3.org/1999/xhtml"
  xmlns="http://www.w3.org/1999/xhtml"
  exclude-result-prefixes="html rstx">

  <xsl:output
    method="html"
    doctype-public="about:legacy-compat"
    omit-xml-declaration="yes"
    encoding="UTF-8"
    indent="yes" />

  <xsl:strip-space elements="*"/>

  <xsl:variable name="path" select="rstx/@path"/>
  <xsl:variable name="site" select="rstx/directory[directory]"/>

  <xsl:include href="body.xsl"/>

  <xsl:template match="/">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="document">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-gb" lang="en-gb">
      <head>
	<meta charset="UTF-8"/>
	<title><xsl:value-of select="title"/></title>
      </head>
      <body>
	<xsl:apply-templates select="$site" mode="nav"/>
	<xsl:apply-templates select="rstx:media()/css" mode="media"/>
	<xsl:apply-templates/>
	<xsl:apply-templates select="rstx:media()/script" mode="media"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="directory" mode="nav">
    <a href="{@path}">
      <xsl:value-of select="@title"/>
    </a>
    <xsl:apply-templates mode="nav"/>
  </xsl:template>

  <xsl:template match="css"  mode="media">
    <xsl:copy-of select="."/>
  </xsl:template>

  <xsl:template match="script"  mode="media">
    <script src="{@src}">
      <xsl:value-of select="' '"/>
    </script>
  </xsl:template>

  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="docinfo"/>

</xsl:stylesheet>