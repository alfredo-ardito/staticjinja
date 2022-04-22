############################### example 1

from jinja2 import Environment, FileSystemLoader
content = 'This is about page'
mystring = "{% extends '_base.html' %}{% block content %}wow{% endblock %}"
file_loader = FileSystemLoader('/home/alfredo.ardito/git-repos/projects/ssg/staticjinja/templates/')
env = Environment(loader=file_loader).from_string(mystring)
data = env.render()
print(data)

############################### example 2

from jinja2 import Environment, FileSystemLoader
mycontent = 'This is about page'
mystring = "{% extends '_base.html' %}{% block content %}wow. {{ mycontent }}{% endblock %}"
file_loader = FileSystemLoader('/home/alfredo.ardito/git-repos/projects/ssg/staticjinja/templates/')
env = Environment(loader=file_loader).from_string(mystring)
data = env.render(mycontent=mycontent)
print(data)

############################### example 3

from jinja2 import Environment, FileSystemLoader
content = 'This is about page'
file_loader = FileSystemLoader('/home/alfredo.ardito/git-repos/projects/ssg/staticjinja/templates/')
env = Environment(loader=file_loader)

import codecs

from jinja2 import nodes, TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import Const
from markdown2 import Markdown


class MarkdownExtension(Extension):
    tags = {'markdown'}
    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdown_dir='markdowns'
        )
    def parse(self, parser):
        line_number = next(parser.stream).lineno
        md_file = [Const('')]
        body = ''
        try:
            md_file = [parser.parse_expression()]
        except TemplateSyntaxError:
            body = parser.parse_statements(['name:endmarkdown'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_to_html', md_file), [], [], body).set_lineno(line_number)
    def _to_html(self, md_file, caller):
        if len(md_file):
            with codecs.open('{}/{}'.format(self.environment.markdown_dir, md_file), 'r', encoding='utf-8') as f:
                return Markdown().convert(f.read())
        else:
            return Markdown().convert(caller())
            
env.add_extension(MarkdownExtension)

template = env.get_template('index.html')
output = template.render(sacalamone=f"{content} from sacalamone")
print(output)

###############################  example 4

from jinja2 import Environment, FileSystemLoader
mycontent = 'This is about page'
file_loader = FileSystemLoader('/home/alfredo.ardito/git-repos/projects/ssg/staticjinja/templates/')
env = Environment(loader=file_loader)

import codecs

from jinja2 import nodes, TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import Const
from markdown2 import Markdown


class MarkdownExtension(Extension):
    tags = {'markdown'}
    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdown_dir='markdowns'
        )
    def parse(self, parser):
        line_number = next(parser.stream).lineno
        md_file = [Const('')]
        body = ''
        try:
            md_file = [parser.parse_expression()]
        except TemplateSyntaxError:
            body = parser.parse_statements(['name:endmarkdown'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_to_html', md_file), [], [], body).set_lineno(line_number)
    def _to_html(self, md_file, caller):
        if len(md_file):
            with codecs.open('{}/{}'.format(self.environment.markdown_dir, md_file), 'r', encoding='utf-8') as f:
                return Markdown().convert(f.read())
        else:
            return Markdown().convert(caller())
            
env.add_extension(MarkdownExtension)

mystring = "{% extends '_base.html' %}{% block content %}wow. {{ sacalamone }} {% markdown 'ABOUT.md' %} {% endblock %}"

newenv = env.from_string(mystring)
data = newenv.render(sacalamone="this is a test from sacalamone")
print(data)

###############################  example 5

from jinja2 import Environment, FileSystemLoader
mycontent = 'This is about page'
file_loader = FileSystemLoader('/home/alfredo.ardito/git-repos/projects/ssg/staticjinja/templates/')
env = Environment(loader=file_loader)

import codecs

from jinja2 import nodes, TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import Const
from markdown2 import Markdown


class MarkdownExtension(Extension):
    tags = {'markdown'}
    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdown_dir='markdowns'
        )
    def parse(self, parser):
        line_number = next(parser.stream).lineno
        md_file = [Const('')]
        body = ''
        try:
            md_file = [parser.parse_expression()]
        except TemplateSyntaxError:
            body = parser.parse_statements(['name:endmarkdown'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_to_html', md_file), [], [], body).set_lineno(line_number)
    def _to_html(self, md_file, caller):
        if len(md_file):
            with codecs.open('{}/{}'.format(self.environment.markdown_dir, md_file), 'r', encoding='utf-8') as f:
                return Markdown().convert(f.read())
        else:
            return Markdown().convert(caller())
            
env.add_extension(MarkdownExtension)

mystring = "{% extends '_base.html' %}{% block content %}wow. {{ sacalamone }} {% markdown 'ABOUT.md' %} {% endblock %}"

newenv = env.from_string(mystring)
env.from_string(mystring).stream(sacalamone="this is a test from sacalamone").dump(str('salamone.html'), encoding="utf-8")



