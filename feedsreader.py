# -*- coding: utf-8 -*-

import datetime
import ssl
import urllib.request
import feedparser

#Extract URLs from public dropbox file.
feedsUrl = "http://mcxvio.gitlab.io/feeds/urls.txt"  # dl=1 is important

def executeFeedReadWrite():

    urls = loadFeedsUrls()
    feedsByDate = readFeedsSortByPublishedDate(urls)

    with open('public/blogroll.md', 'w') as output:
        outputDocumentHeader(output)
        output.write("\n")

        for item in feedsByDate:
            outputFeedTitleEntry(item, output)

        output.write("\n")
        output.write('<p class="footer"><br><br>Page updated: {:%Y-%m-%d %H:%M:%S}</p>'.format(datetime.datetime.now()))

def outputFeedTitleEntry(item, output):
    output.write("### ")
    output.write("[" + item['title'] + "]")
    output.write("(" + item['title_link'] + ")")
    output.write("\n")
    output.write("* #### ")
    output.write("[" + item['entry_title'].decode('utf-8') + "]")
    output.write("(" + item['entry_link'] + ")")
    output.write("\n")
    if item['entry_date'] != "":
        output.write("<p class='footer'>" + item['entry_date'] + "</p>")
        output.write("\n")
        output.write("\n")
    output.write("\n")

def outputDocumentHeader(output):
    output.write("Title: Blogroll")
    output.write("\n")
    output.write("Category: People, Process, Products")
    output.write("\n")
    output.write("Tags: process, products, people, blogroll")
    output.write("\n")
    output.write("Slug: blogroll")
    output.write("\n")

def feedEntryPublishedDate(d):
    entryDate = ""
    if "published" in d.entries[0].keys():
        entryDate = d.entries[0].published_parsed
    else:
        if "updated" in d.entries[0].keys():
            entryDate = d.entries[0].updated_parsed

    if entryDate != "":
        dt = datetime.datetime(*(entryDate[0:6]))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return entryDate

def feedTitle(d):
    if "title" in d.feed.keys():
        return d.feed.title
    else:
        return d.feed.description

def readFeedsSortByPublishedDate(urls):
    #List of feed items.
    feedsList = []

    for line in urls.splitlines():
        url = line.decode("utf-8")
        d = feedparser.parse(url)

        feedsList.append({ "title": feedTitle(d),
                 "title_link": d.feed.link,
                 "entry_title": d.entries[0].title.encode('utf-8'),
                 "entry_link": d.entries[0].link,
                 "entry_date": feedEntryPublishedDate(d) })

    #Show feed's newest entry first (https://stackoverflow.com/questions/5055812/sort-python-list-of-objects-by-date).
    return sorted(feedsList, key=lambda k: k['entry_date'], reverse=True)

def loadFeedsUrls():
    #http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
    ssl._create_default_https_context = ssl._create_unverified_context

    with urllib.request.urlopen(feedsUrl) as response:
        urls = response.read()

    return urls

if __name__ == '__main__':
    print("Working...")
    executeFeedReadWrite()
    print("...Done")
