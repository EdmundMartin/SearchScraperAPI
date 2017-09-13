# SearchScraperAPI

Search Scraper API is an implementation of an API, which allows you to scrape Google, Bing, with plans to add support for other search engines. The async server provides to endpoints where users can post keywords and other parameters. This scraper service is perfect those in SEO or for those looking to scrape a large number of results from popular search engines.

## Starting the server

Coming soon.

## Google Scraping

```python
import requests

# Grabs a ten results from Google - for the term "Python Google Scraper" using geo "GB - aka Great Britain".
res = requests.post('http://127.0.0.1:8080/google-scrape', json={"keyword": "Python Google scraper", "geo": "GB",
                                                                 "number": 10, "proxy": "109.169.6.152:8080"})
```
To scrape Google, a user sends a post-request to the "/google-scrape" endpoint. The endpoint takes four arguments, keyword (string), geo (string), number (integer), and a proxy (string). The results are then returned should there be no error. 

### Parameters
* keyword - string, required
* geo - string, optional will use Google.com if no valid geo is provided.
* number - integer, any integer from 1 to 100.
* proxy - string
