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
