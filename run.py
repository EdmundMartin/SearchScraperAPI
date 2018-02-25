from searchscrapeserver import SearchScraper

if __name__ == '__main__':
    server = SearchScraper('127.0.0.1', 8080)
    server.run_server()