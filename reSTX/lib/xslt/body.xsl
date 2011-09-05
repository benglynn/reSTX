<xsl:stylesheet 
    version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:rstx="http://benglynn.net/rstx"
  xmlns:html="http://www.w3.org/1999/xhtml"
  xmlns="http://www.w3.org/1999/xhtml"
  exclude-result-prefixes="html rstx">

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
    <xsl:element name="{rstx:heading_name(.)}">
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>

  <xsl:template match="paragraph">
    <p>
      <xsl:apply-templates />
    </p>
  </xsl:template>

  <xsl:template match="literal_block">
    <pre><xsl:apply-templates /></pre>
  </xsl:template>

  <xsl:template match="reference[@refuri]">
    <a href="{@refuri}">
      <xsl:apply-templates/>
    </a>
  </xsl:template>

</xsl:stylesheet>