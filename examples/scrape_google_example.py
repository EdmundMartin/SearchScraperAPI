import requests
from time import sleep
import csv
'''Assumes that an instance of the SearchScraperAPI is running on http://127.0.0.1:8080/'''

keywords = ['Python google scraper', 'google seo rank checker', 'rank checker']
results = []


for keyword in keywords:
    r = requests.post('http://127.0.0.1:8080/google-scrape', json={'keyword': keyword, 'geo': 'GB'}).json()
    if 'error' not in r:
        results.append(r)
    sleep(10)

headers = results[0]['results'][0].keys()
with open('output.csv', 'a', encoding='utf-8') as output_file:
    writer = csv.DictWriter(output_file, headers)
    writer.writeheader()
    for result in results:
        data = result['results']
        writer.writerows(data)