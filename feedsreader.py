"""
Load a file of feed urls, fetch feed data and format for output to MarkDown doc.
"""
# -*- coding: utf-8 -*-
import datetime
import ssl
import urllib.request
from urllib.parse import urlparse
import feedparser
#Extract URLs from public dropbox file.
FEEDS_URL = "http://mcxvio.gitlab.io/feeds/urls.txt"  # dl=1 is important

def execute_feed_read_write():
    """ Method details here. """
    urls = load_feeds_urls()
    feeds_by_date = read_feeds_sort_pub_date(urls)

    with open('public/blogroll.md', 'w') as output:
        output_document_header(output)
        output.write("\n")

        for item in feeds_by_date:
            output_feed_title_entry(item, output)

        output.write("\n")
        updated_text = '<p class="footer"><br><br>Page updated: '
        updated_date = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        output.write(updated_text + updated_date + '</p>')

def load_feeds_urls():
    """ Method details here. """
    #//stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
    ssl._create_default_https_context = ssl._create_unverified_context
    with urllib.request.urlopen(FEEDS_URL) as response:
        urls = response.read()
    return urls

def read_feeds_sort_pub_date(urls):
    """ Method details here. """
    #List of feed items.
    feeds_list = []
    for line in urls.splitlines():
        data = parse_feed_url(line)
        feeds_list.append(load_feeds_output_info(data))

    #Show feed's newest entry first
    #//stackoverflow.com/questions/5055812/sort-python-list-of-objects-by-date
    return sorted(feeds_list, key=lambda k: k['entry_date'], reverse=True)

def parse_feed_url(line):
    """ Method details here. """
    url = line.decode("utf-8")
    return feedparser.parse(url)

def load_feeds_output_info(data):
    """ Method details here. """
    return {"title": feed_title(data),
            "title_link": data.feed.link,
            "entry_title": data.entries[0].title.encode('utf-8'),
            "entry_link": data.entries[0].link,
            "entry_date": feed_entry_published_date(data)}

def feed_title(data):
    """ Method details here. """
    title = ""
    if "title" in data.feed.keys():
        title = data.feed.title
    if "description" in data.feed.keys() and title == "":
        title = data.feed.description
    if title == "":
        #Slice the feed's url if title is empty.
        output = urlparse(data.feed.link)
        title = output.netloc
    return title

def feed_entry_published_date(data):
    """ Method details here. """
    entry_date = ""
    if "published" in data.entries[0].keys():
        entry_date = data.entries[0].published_parsed
    else:
        if "updated" in data.entries[0].keys():
            entry_date = data.entries[0].updated_parsed

    if entry_date != "":
        date_time = datetime.datetime(*(entry_date[0:6]))
        return date_time.strftime('%Y-%m-%d %H:%M:%S')

def output_document_header(output):
    """ Method details here. """
    output.write("Title: Blogroll")
    output.write("\n")
    output.write("Category: People, Process, Products")
    output.write("\n")
    output.write("Tags: process, products, people, blogroll")
    output.write("\n")
    output.write("Slug: blogroll")
    output.write("\n")

def output_feed_title_entry(item, output):
    """ Method details here. """
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

if __name__ == '__main__':
    print("Working...")
    execute_feed_read_write()
    print("...Done")
