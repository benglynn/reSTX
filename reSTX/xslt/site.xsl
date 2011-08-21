<xsl:stylesheet 
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output
    method="html"
    doctype-public="about:legacy-compat"
    omit-xml-declaration="yes"
    encoding="UTF-8"
    indent="yes" />

  <xsl:strip-space elements="*"/>

  <xsl:include href="body.xsl"/>

  <xsl:template match="/">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="document">
    <html>
      <head>
	<meta charset="UTF-8"/>
	<title><xsl:value-of select="title"/></title>
      </head>
      <body>
	<xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="docinfo"/>

</xsl:stylesheet>