<xsl:stylesheet 
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <xsl:apply-templates select="document"/>
  </xsl:template>

<xsl:template match="document">
    <html>
      <head>
	<title><xsl:value-of select="title"/></title>
      </head>
      <body>
	<h1><xsl:value-of select="title"/></h1>
	<xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="*"/>

</xsl:stylesheet>