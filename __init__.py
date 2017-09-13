from server.server import SearchScraper


if __name__ == '__main__':
    scraping = SearchScraper()
    scraping.run_server()