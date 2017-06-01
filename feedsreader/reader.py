# -*- coding: utf-8 -*-

#Extract URLs from public dropbox file.
url = "http://www.dropbox.com/s/yuo52behpqchn39/TechFeedURLs.txt?dl=1"  # dl=1 is important

import ssl
import urllib.request
import feedparser

print("Working...")

#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
ssl._create_default_https_context = ssl._create_unverified_context

with urllib.request.urlopen(url) as response:
    html = response.read()

with open('output/blogroll.md', 'w') as output:
    #output.write("hello markdown file")
    output.write("Title: Blogroll")
    output.write("\n")
    for line in html.splitlines():
        url = line.decode("utf-8")
        #Get RSS for each URL.
        d = feedparser.parse(url)
        #Extract latest story.
        #output.write("\n")
        #output.write(url)
        output.write("[" + d.entries[0].title + "]")
        output.write("(" + d.entries[0].link + ")")
        output.write("\n")
        output.write(d.entries[0].description[0:100])
        #output.write("\n")
        output.write("\n")
    output.close

print(output.closed)
