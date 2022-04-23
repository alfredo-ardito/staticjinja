---
# 1) If layout is set and the layout name starts with the underscore
# it will then use the inline string which extends the template rendering.
# example: 
# mylayout = "{% extends '_base.html' %} \
# {% block content %}wow. {{ sacalamone }} {% markdown 'ABOUT.md' %} \
# {% endblock %}"
#
# 2) If layout is set without the underscore at the beggining
# it will then use the layout name as the templete name to rendere the page.
layout: _base.html
context: markdown_content
pagename: servizi.html
---

SERVICE.md
==========

## Sub-heading

Paragraphs are separated
by a blank line.

Two spaces at the end of a line  
produces a line break.

Text attributes _italic_, **bold**, `monospace`.

# New line here B

this is a new line....:::

