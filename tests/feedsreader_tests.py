"""
Test the feedsreader module.
"""
# -*- coding: utf-8 -*-
import os
from os import path
import shutil
import sys
import tempfile
import unittest
import urllib.request

#Run tests from root directory.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR.endswith('/tests'):
    ROOT_DIR = ROOT_DIR[:-6]
sys.path.insert(1, ROOT_DIR)
import feedsreader

class TestFeedsReader(unittest.TestCase):
    """
    Test the feedsreader module.
    """
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_urls_file_exists(self):
        """
        Test the file, which contains the urls, exists.
        """
        url = urllib.request.urlopen(feedsreader.FEEDS_URL)
        self.assertTrue(url.getcode() == 200)

    def test_load_feeds_urls_get_feed(self):
        """
        Test loading and parsing the feed from the first url in the file.
        """
        urls = feedsreader.load_feeds_urls()
        self.assertTrue(len(urls) > 1)

        url = urls.splitlines()[0]
        data = feedsreader.parse_feed_url(url)
        self.assertTrue(data.feed is not None)

        info = feedsreader.load_feeds_output_info(data)
        self.assertTrue(info.get('title') != "")
        self.assertTrue(info.get('title_link') != "")
        self.assertTrue(info.get('entry_title') != "")
        self.assertTrue(info.get('entry_link') != "")
        self.assertTrue(info.get('entry_date') != "")

    def test_feed_entries_date_sort(self):
        """
        Test sorting the feeds by entry date.
        """
        urls = feedsreader.load_feeds_urls()
        self.assertTrue(len(urls) > 1)

        feeds_by_date = feedsreader.read_feeds_sort_pub_date(urls)
        entry_0 = feeds_by_date[0].get('entry_date')
        entry_1 = feeds_by_date[1].get('entry_date')
        self.assertTrue(entry_0 > entry_1)

    def test_retrieve_header_output(self):
        """
        Test writing to an output file.
        """
        # Create a file in the temporary directory to test output methods.
        with open(path.join(self.test_dir, 'test.txt'), 'w') as test_file:
            feedsreader.output_document_header(test_file)

        # Reopen temp file & check if what we read back is the same as expected.
        with open(path.join(self.test_dir, 'test.txt')) as test_file:
            test_file_header = 'Title: Blogroll\n'
            test_file_header += 'Category: People, Process, Products\n'
            test_file_header += 'Tags: process, products, people, blogroll\n'
            test_file_header += 'Slug: blogroll\n'
            self.assertEqual(test_file.read(), test_file_header)


if __name__ == '__main__':
    unittest.main()
