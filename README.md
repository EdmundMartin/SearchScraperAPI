# SearchScraperAPI

Search Scraper API is an implementation of an API, which allows you to scrape Google, Bing, with plans to add support for other search engines. The async server provides to endpoints where users can post keywords and other parameters. This scraper service is perfect those in SEO or for those looking to scrape a large number of results from popular search engines.

## Examples
```python
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
```
The above example demonstrates requests being made to the server, dispatched using requests and the concurrent futures. When used as above the server should respond with results almost simultanousely. There is a significant chance of being block should you not use a pool of proxies, as the rapid firing of requests will set off bot detection. 

## Google Scraping

```python
import requests

# Grabs a ten results from Google - for the term "Python Google Scraper" using geo "uk - aka Great Britain".
res = requests.post('http://127.0.0.1:8080/google-scrape', json={"keyword": "Python Google scraper", "geo": "uk",
                                                                 "number": 10, "proxy": "109.169.6.152:8080"})
```
To scrape Google, a user sends a post-request to the "/google-scrape" endpoint. The endpoint takes four arguments, keyword (string), geo (string), number (integer), and a proxy (string). The results are then returned should there be no error. 

### Parameters
* keyword - string, required
* geo - string, optional will use Google.com if no valid geo is provided.
* number - integer, any integer from 1 to 100.
* proxy - string

### Result
```json
{
    "geo": "GB",
    "keyword": "Python Google Scraping",
    "results": [
        {
            "title": "GitHub - NikolaiT/GoogleScraper: A Python module to scrape several ...",
            "rank": 1,
            "url": "https://github.com/NikolaiT/GoogleScraper",
            "description": "A Python module to scrape several search engines (like Google, Yandex, Bing, Duckduckgo, Baidu and others) by using proxies (socks4/5, http proxy) and with ..."
        },
        {
            "title": "Google Search Web Scraping with Python - Stack Overflow",
            "rank": 2,
            "url": "https://stackoverflow.com/questions/38619478/google-search-web-scraping-with-python",
            "description": "27 Jul 2016 - You can always directly scrape Google results. To do this, you can use the URL https://google.com/search?q=<Query> this will return the top 10 ..."
        },
        {
            "title": "python - How to scrape more than 100 google pages in one pass ...",
            "rank": 3,
            "url": "https://stackoverflow.com/questions/34614057/how-to-scrape-more-than-100-google-pages-in-one-pass",
            "description": "5 Jan 2016 - You can use a more programmatic api from google to get the results vs. trying to screen scrape the human search interface, there's no error ..."
        },
        {
            "title": "Scraping and parsing Google search results using Python - Stack ...",
            "rank": 4,
            "url": "https://stackoverflow.com/questions/7746832/scraping-and-parsing-google-search-results-using-python",
            "description": "12 Oct 2011 - You may find xgoogle useful... much of what you seem to be asking for is there..."
        },
        {
            "title": "GoogleScraper 0.2.1 : Python Package Index",
            "rank": 5,
            "url": "https://pypi.python.org/pypi/GoogleScraper/0.2.1",
            "description": "4 Dec 2015 - A module to scrape and extract links, titles and descriptions from various search engines. Supports google,bing,yandex and many more."
        },
        {
            "title": "google-search 1.0.2 : Python Package Index",
            "rank": 6,
            "url": "https://pypi.python.org/pypi/google-search",
            "description": "12 May 2017 - google-search. Library for scraping google search results. Usage: from googlesearch.googlesearch import GoogleSearch response ..."
        },
        {
            "title": "How to effectively scrape google search results - YouTube",
            "rank": 7,
            "url": "https://www.youtube.com/watch?v=56dUrErkPk8",
            "description": "Python video showing how to effectively scrape google search results to get back relevant data for your ..."
        },
        {
            "title": "Python Tutorial - Google Scraper Thousands of URLs in Seconds ...",
            "rank": 8,
            "url": "https://www.youtube.com/watch?v=Hrs1n76JN6I",
            "description": "In this video, I will show you how to scrape thousands of google search results in a matter of seconds. The ..."
        },
        {
            "title": "Web Scraping - Automate the Boring Stuff with Python",
            "rank": 9,
            "url": "https://automatetheboringstuff.com/chapter11/",
            "description": "For example, Google runs many web scraping programs to index web pages for its ... A web browser tab will open to the URL http://inventwithpython.com/."
        }
    ]
}
```
## Bing
```python
import requests

# Grabs a ten results from Bing - for the term "Python Google Scraper" using geo "uk - aka Great Britain".
res = requests.post('http://127.0.0.1:8080/bing-scrape', json={"keyword": "Python Google scraper", "geo": "uk",
                                                                 "number": 10, "proxy": "109.169.6.152:8080"})
```
To scrape Google, a user sends a post-request to the "/bing-scrape" endpoint. The endpoint takes four arguments, keyword (string), geo (string), number (integer), and a proxy (string). The results are then returned should there be no error. 

### Parameters
* keyword - string, required
* geo - string, optional will use Bing.com if no valid geo is provided.
* number - integer, any integer from 1 to 50.
* proxy - string

### Result
```json
{
    "results": [
        {
            "url": "https://pypi.python.org/pypi/GoogleScraper/0.2.1",
            "title": "GoogleScraper 0.2.1 : Python Package Index",
            "description": "A module to scrape and extract links, titles and descriptions from various search engines. Supports google,bing,yandex and many more.",
            "rank": 1
        },
        {
            "url": "https://pypi.python.org/pypi/GoogleScraper/0.1.2",
            "title": "GoogleScraper 0.1.2 : Python Package Index",
            "description": "A module to scrape and extract links, titles and descriptions from Google search results. Latest Version: 0.2.1 ## GoogleScraper - Scraping the Google Search Engine",
            "rank": 2
        },
        {
            "url": "https://stackoverflow.com/questions/11513624/python-google-search-scraper-with-beautifulsoup",
            "title": "screen scraping - python: Google Search Scraper with ...",
            "description": "Goal: Pass a search string to search on google and scrape url, title and the small description that get publish along with the url title. I have following code and at ...",
            "rank": 3
        },
        {
            "url": "https://mukarramkhalid.com/python-making-your-own-google-scraper-mass-exploiter/",
            "title": "[Python] Making Your Own Google Scraper & Mass Exploiter",
            "description": "In this Step by Step Tutorial, I'll show you how to make your own Google Scraper (Dork Scanner) and Mass Vulnerability Scanner / Exploiter in Python. MakMan",
            "rank": 4
        },
        {
            "url": "https://github.com/NikolaiT/GoogleScraper",
            "title": "GitHub - NikolaiT/GoogleScraper: A Python module to scrape ...",
            "description": "GoogleScraper - A Python module to scrape several search engines (like Google, Yandex, Bing, Duckduckgo, Baidu and others) by …",
            "rank": 5
        },
        {
            "url": "https://stackoverflow.com/questions/38619478/google-search-web-scraping-with-python",
            "title": "Google Search Web Scraping with Python - Stack Overflow",
            "description": "I've been learning a lot of python lately to work on some projects at work. Currently I need to do some web scraping with google search results. I found several sites ...",
            "rank": 6
        },
        {
            "url": "https://stackoverflow.com/questions/15550655/web-scraping-google-news-with-python",
            "title": "web scraping google news with python - Stack Overflow",
            "description": "I am creating a web scraper for different news outlets, for Nytimes and the Guardian it was easy since they have their own API. Now, I want to scrape results from ...",
            "rank": 7
        },
        {
            "url": "https://stackoverflow.com/questions/34479656/scrape-google-with-python-what-is-the-correct-url-for-requests-get",
            "title": "Scrape Google with Python - What is the correct URL …",
            "description": "Goal: I would like to verify, if a specific Google search has a suggested result on the right hand side and - in case of such a suggestion - scrape some information ...",
            "rank": 8
        },
        {
            "url": "https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search",
            "title": "web scraping - Python - Download Images from google Image ...",
            "description": "I want to download all Images of google image search using python . The code I am using seems to have some problem some times …",
            "rank": 9
        },
        {
            "url": "https://stackoverflow.com/questions/7746832/scraping-and-parsing-google-search-results-using-python",
            "title": "Scraping and parsing Google search results using Python ...",
            "description": "I asked a question on realizing a general idea to crawl and save webpages. Part of the original question is: how to crawl and save a lot of \"About\" pages from the ...",
            "rank": 10
        }
    ],
    "geo": "GB",
    "keyword": "Python Google Scraping"
}
```
