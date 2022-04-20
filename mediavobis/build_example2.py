from staticjinja import Site

import codecs

from jinja2 import nodes, TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import Const
from markdown2 import Markdown

from pathlib import Path

_searchpath = 'templates'
_outpath = '.'
_markdown_dir = f'{_searchpath}/markdowns' 

class MarkdownExtension(Extension):
    tags = {'markdown'}

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)
        environment.extend(
            markdown_dir = _markdown_dir
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


if __name__ == "__main__":

    class MySite(Site):
        def __init__(
                self,
                environment,
                searchpath,
                outpath=".",
                encoding="utf8",
                logger=None,
                contexts=None,
                rules=None,
                staticpaths=None,
                mergecontexts=False,
            ):
            super().__init__(
                environment,
                searchpath,
                outpath,
                encoding,
                logger,
                contexts,
                rules,
                staticpaths,
                mergecontexts,)

        def is_markdown(self, filename):
            return any(part.endswith(".md") for part in Path(filename).parts)

        def get_dependents(self, filename):
            if self.is_partial(filename):
                return self.template_names
            elif self.is_markdown(filename):
                return self.template_names
            elif self.is_template(filename):
                return [filename]
            elif self.is_static(filename):
                return [filename]
            else:
                return []


    site = MySite.make_site(
        searchpath = _searchpath,
        outpath = _outpath,
        extensions=[MarkdownExtension],)
    # enable automatic reloading
    site.render(use_reloader=True)
    #site.render(use_reloader=False)

