print("hello world")

import feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
        #feed = feedparser.parse(rss) #<<WORKS!!
        d = feedparser.parse('https://martinfowler.com/feed.atom')

#d = feedparser.parse('https://medium.mybridge.co/feed')
#d = feedparser.parse('http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml')

#https://medium.mybridge.co/feed
#https://martinfowler.com/feed.atom
#http://www.enterpriseintegrationpatterns.com/ramblings.rss
#https://weblogs.asp.net/scottgu/rss?containerid=13
#https://kenschwaber.wordpress.com/?feed=rss
#https://feeds.feedburner.com/codinghorror
#http://feeds.hanselman.com/ScottHanselman
#http://www.codeproject.com/WebServices/ArticleRSS.aspx

print(d.entries[0].title)
print(d.entries[0].keys())

if "published" in d.entries[0].keys():
    print(d.entries[0].published)
else:
    print(d.entries[0].updated)

print(d.entries[0].summary)
#print(d['channel']['item'])

print("all good")
