import os, shutil, sys, tempfile
from os import path
import unittest

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

    def test_load_feeds_returns_html(self):
        html = feedsreader.loadFeeds()
        self.assertTrue(len(html) > 0)
        print(html)

    def test_retrieve_document_header_output(self):
        # Create a file in the temporary directory to test output methods.
        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            feedsreader.outputDocumentHeader(f)

        # Reopen the temp file and check if what we read back is the same as expected.
        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(f.read(), 'Title: Blogroll\nCategory: People, Process, Products\nTags: process, products, people, blogroll\nSlug: blogroll\n')

if __name__ == '__main__':
    unittest.main()
