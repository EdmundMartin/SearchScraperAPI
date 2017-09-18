import unittest
import os

from parsing.bing_result_parser import parse_html as bing_parse_html
from parsing.google_result_parser import parse_html as google_parse_html
from parsing.yandex_result_parser import parse_html as yandex_parse_html


class TestYandexParser(unittest.TestCase):

    def setUp(self):
        self.html = ''
        with open(os.path.join(os.getcwd(),'html_samples/yandex.html'), 'r', encoding='utf-8') as html_file:
            for line in html_file:
                self.html += line

    def test_yandex_html(self):
        results = yandex_parse_html(self.html)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], dict)
        self.assertEqual(results[0]['url'], 'https://github.com/NikolaiT/GoogleScraper')
        self.assertEqual(len(results), 10)


class TestGoogleParser(unittest.TestCase):

    def setUp(self):
        self.html = ''
        with open(os.path.join(os.getcwd(),'html_samples/google.html'), 'r', encoding='utf-8') as html_file:
            for line in html_file:
                self.html += line

    def test_google_html(self):
        results = google_parse_html(self.html)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], dict)
        self.assertEqual(results[0]['url'], 'https://github.com/NikolaiT/GoogleScraper')
        self.assertEqual(len(results), 99)


class TestBingParser(unittest.TestCase):

    def setUp(self):
        self.html = open(os.path.join(os.getcwd(),'html_samples/bing.html'), 'r', encoding='utf-8').read()

    def test_bing_html(self):
        results = bing_parse_html(self.html)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], dict)
        self.assertEqual(results[0]['url'], 'https://github.com/NikolaiT/GoogleScraper')
        self.assertEqual(len(results), 48)