import unittest
from scraping.bing_scraping import build_bing_url, unpack_data

class TestBingScraping(unittest.TestCase):

    def test_build_url_with_geo(self):
        url = build_bing_url('gb', 'python', 50)
        self.assertEqual(url, 'http://www.bing.com/search?q=python&count=50')

    def test_build_url_without_geo(self):
        url = build_bing_url('blah', 'python', 50)
        self.assertEqual(url, 'http://www.bing.com/search?q=python&count=50')

    def test_unpack_data_no_proxy(self):
        data = {'keyword': 'python', 'geo': 'gb', 'number': 50}
        keyword, geo, number, proxy = unpack_data(data)
        self.assertEqual(keyword, 'python')
        self.assertEqual(geo, 'gb')
        self.assertEqual(number, 50)
        self.assertEqual(proxy, None)

    def test_unpack_data(self):
        data = {'keyword': 'python', 'geo': 'gb', 'number': 50, 'proxy': '127.0.0.1:8080'}
        keyword, geo, number, proxy = unpack_data(data)
        self.assertEqual(keyword, 'python')
        self.assertEqual(geo, 'gb')
        self.assertEqual(number, 50)
        self.assertEqual(proxy, '127.0.0.1:8080')