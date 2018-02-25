from searchscrapeserver import SearchScraper

if __name__ == '__main__':
    server = SearchScraper('0.0.0.0', 5000)
    server.run_server()