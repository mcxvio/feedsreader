#!/usr/bin/python
print "Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"
print "Test Page"
print "</body></html>"

url = "http://www.dropbox.com/s/yuo52behpqchn39/TechFeedURLs.txt?dl=1"  # dl=1 is important

'''
import ssl
import urllib.request
import feedparser

#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
ssl._create_default_https_context = ssl._create_unverified_context

with urllib.request.urlopen(url) as response:
    html = response.read()

for line in html.splitlines():
    url = line.decode("utf-8")
    #Get RSS for each URL.
    d = feedparser.parse(url)
    #Extract latest story.
    print(url)
    print(d.entries[0].title)
'''

import jinja2
from jinja2 import Template
#Send to Jinja temlate for reading.
template = Template('Hello {{ name }}!')
print(template.render(name='John Doe'))

print "all good"