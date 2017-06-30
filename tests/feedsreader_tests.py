import feedparser
import os, shutil, sys, tempfile
from os import path
import unittest
import urllib.request

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR.endswith('/tests'):
    ROOT_DIR = ROOT_DIR[:-6]
sys.path.insert(1, ROOT_DIR)

import feedsreader

class TestFeedsReader(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_urls_file_exists(self):
        url = urllib.request.urlopen(feedsreader.feedsUrl)
        self.assertTrue(url.getcode() == 200)

    def test_load_feeds_urls_return_first_feeds_info(self):
        urls = feedsreader.loadFeedsUrls()
        self.assertTrue(len(urls) > 1)

        url = urls.splitlines()[0]
        d = feedsreader.parseFeedUrl(url)
        self.assertTrue(d.feed is not None)

        info = feedsreader.loadFeedsOutputInfo(d)
        self.assertTrue(info.get('title') != "")
        self.assertTrue(info.get('title_link') != "")
        self.assertTrue(info.get('entry_title') != "")
        self.assertTrue(info.get('entry_link') != "")
        self.assertTrue(info.get('entry_date') != "")

    def test_feed_entries_sorted_by_date(self):
        urls = feedsreader.loadFeedsUrls()
        self.assertTrue(len(urls) > 1)

        feedsByDate = feedsreader.readFeedsSortByPublishedDate(urls)
        self.assertTrue(feedsByDate[0].get('entry_date') > feedsByDate[1].get('entry_date'))

    def test_retrieve_document_header_output(self):
        # Create a file in the temporary directory to test output methods.
        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            feedsreader.outputDocumentHeader(f)

        # Reopen the temp file and check if what we read back is the same as expected.
        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(f.read(), 'Title: Blogroll\nCategory: People, Process, Products\nTags: process, products, people, blogroll\nSlug: blogroll\n')


if __name__ == '__main__':
    unittest.main()
