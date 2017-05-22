# -*- coding: utf-8 -*-

#Send to Jinja template for reading.

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('reader', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('index.html')
print(template.render(title='hello world'))

###Create markup that can then be turned to html by pelican?
