from concurrent.futures import ThreadPoolExecutor
import requests

'''Assumes that an instance of the SearchScraperAPI is running on http://127.0.0.1:8080/
    Implementing such a scraper will run a high risk of being banned should the user not rotate the
    proxies used from a centralised pool.
'''

keywords = ['google scraping', 'google rank checker', 'scrape google']


def post_to_server(keyword):
    r = requests.post('http://127.0.0.1:8080/bing-scrape', json={'keyword': keyword})
    return r.text

with ThreadPoolExecutor(max_workers=3) as executor:
    jobs = [executor.submit(post_to_server, keyword) for keyword in keywords]
    results = [job.result() for job in jobs]
    for result in results:
        print(result)