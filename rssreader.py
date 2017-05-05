#Extract URLs from public dropbox file.
url = "http://www.dropbox.com/s/yuo52behpqchn39/TechFeedURLs.txt?dl=1"  # dl=1 is important

import ssl
import urllib.request
import feedparser

#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as response:
    html = response.read()

for line in html.splitlines():
    url = line.decode("utf-8")
    print(url)

    #Get RSS for each URL.
    d = feedparser.parse(url)
    #Extract latest story.
    print(d.entries[0].title)

#Send to Jinja temlate for reading.


###Create markup that can then be turned to html by pelican?
