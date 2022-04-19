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
