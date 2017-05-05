print("hello world")

import feedparser

d = feedparser.parse('http://feeds.feedburner.com/AyendeRahien')
#d = feedparser.parse('http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml')

#http://www.enterpriseintegrationpatterns.com/ramblings.rss
#https://weblogs.asp.net/scottgu/rss?containerid=13
#https://kenschwaber.wordpress.com/?feed=rss
#https://feeds.feedburner.com/codinghorror
#http://feeds.hanselman.com/ScottHanselman
#http://www.codeproject.com/WebServices/ArticleRSS.aspx

print(d.entries[0].title)
#print(d['channel']['item'])

print("all good")

