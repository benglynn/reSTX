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
	<xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="section">
    <section>
      <xsl:apply-templates/>
    </section>
  </xsl:template>

  <xsl:template match="literal">
    <code><xsl:apply-templates/></code>
  </xsl:template>

  <xsl:template match="bullet_list">
    <ul>
      <xsl:apply-templates/>
    </ul>
  </xsl:template>

  <xsl:template match="list_item">
    <li>
      <xsl:apply-templates/>
    </li>
  </xsl:template>

  <xsl:template match="title">
    <h1><xsl:value-of select="text()"/></h1>
  </xsl:template>

  <xsl:template match="paragraph">
    <p>
      <xsl:apply-templates />
    </p>
  </xsl:template>

  <xsl:template match="*"/>

</xsl:stylesheet>