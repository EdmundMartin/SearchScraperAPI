# SearchScraperAPI

Search Scraper API is an implementation of an API, which allows you to scrape Google, Bing, Yandex, and DuckduckGo with plans to add support for other search engines. The async server provides to endpoints where users can post keywords and other parameters. This scraper service is perfect those in SEO or for those looking to scrape a large number of results from popular search engines.

## Running The Server
The easiet way to run the server is to use the included Dockerfile which will build the service and run itself on port 5000 by default.
```
docker build -t server:latest .
```
Simply build the server using the Dockerfile and then run the Docker image as follows:
```
docker run -d -p 5000:5000 server:latest
```
This will allow you to get the server up and running in a couple of minutes and you will then be able to start scraping some of the world's most popular search engines.

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

## Yandex
The search scraper API, also supports Yandex. Yandex offers significantly less regions than both Google & Bing. Yandex also takes an additional optional parameter, with users being able to pass in an "lr" variable which customises the location from which the search is made. If no "lr" is used the search scraper server automatically uses the code for London. The list of all supported codes can be found in the documentation for the Yandex Search API.
### Parameters 
* keyword - string, required
* geo - string, optional will use Bing.com if no valid geo is provided.
* number - integer, any integer from 1 to 50.
* proxy - string
* lr - string.
### Results
```json
{
    "results": [
        {
            "url": "https://github.com/NikolaiT/GoogleScraper",
            "title": "1GitHub - NikolaiT/GoogleScraper: A Python module to scrape...",
            "description": "A Python module to scrape several search engines (like Google, Yandex, Bing, Duckduckgo, Baidu and others) by using proxies (socks4/5, http proxy)...",
            "rank": 1
        },
        {
            "url": "https://www.dataquest.io/blog/web-scraping-tutorial-python/",
            "title": "2Python Web Scraping Tutorial using BeautifulSoup",
            "description": "Web scraping allows us to extract information from web pages. In this tutorial, you’ll learn how to perform web scraping with Python.",
            "rank": 2
        },
        {
            "url": "http://docs.python-guide.org/en/latest/scenarios/scrape/",
            "title": "3HTML Scraping — The Hitchhiker's Guide to Python",
            "description": "Web Scraping. lxml and Requests. Related Topics. ... Python 3, the new best practice, is here to stay. Python 2 will retire in only months!",
            "rank": 3
        },
        {
            "url": "http://www.trackers.clubpenguinaccess.com/vmiaw/lsoeiw.php?vm=bing-scraper-python",
            "title": "4Bing scraper python",
            "description": "Running. Python seach result scraper from: Google, Bing ... Supports google,bing,yandex and many more. Menu Web Scraping and Crawling Are Perfectly Legal, Right?day before yesterday",
            "rank": 4
        },
        {
            "url": "https://www.beyondtheboxscore.com/2015/9/24/9374949/a-new-python-based-pitchf-x-parser-scraper",
            "title": "5A new Python-based PITCHf/x parser & scraper",
            "description": "I've created something to fill that role: a Python-based PITCHf/x scraper that includes much (if not all) of the extra information.",
            "rank": 5
        },
        {
            "url": "https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe",
            "title": "6How to scrape websites with Python and BeautifulSoup",
            "description": "We’ll make data extraction easier by building a web scraper to retrieve stock indices automatically from the Internet. ... We are going to use Python as our scraping language...",
            "rank": 6
        },
        {
            "url": "http://www.exclusivebeatsonly.com/ronyqw/cktsow.php?sw=google-url-scraper-python",
            "title": "7Google url scraper python",
            "description": "popular and powerful Python scraping our scraper a single URL to start from: http ... per page, you can A Python module to scrape several search engines (like Google, Yandex...",
            "rank": 7
        },
        {
            "url": "https://stackoverflow.com/questions/2081586/web-scraping-with-python",
            "title": "8Web scraping with Python - Stack Overflow",
            "description": "I'd like to grab daily sunrise/sunset times from a web site. Is it possible to scrape web content with Python? what are the modules used? Is there any tutorial available?",
            "rank": 8
        },
        {
            "url": "https://elitedatascience.com/python-web-scraping-libraries",
            "title": "95 Tasty Python Web Scraping Libraries",
            "description": "Web scraping is a common and effective way of collecting data for projects and for work. In this guide, we’ll be touring the essential stack of Python web scraping libraries.",
            "rank": 9
        },
        {
            "url": "https://www.safaribooksonline.com/library/view/web-scraping-with/9781491910283/ch01.html",
            "title": "101. Your First Web Scraper - Web Scraping with Python [Book]",
            "description": "Chapter 1. Your First Web Scraper Once you start web scraping, you start to ... The Web, without a layer of ... - Selection from Web Scraping with Python [Book].",
            "rank": 10
        }
    ],
    "keyword": "Python Yandex scraper",
    "geo": "ru"
}
```

## Potential Uses
* Keyword ranking, with a sufficient supply of proxies the server can be used to scrape data for a large number of keywords. This data is frequently used by digital marketing and SEO agencies to demonstrate organic performance.
* Data aggregation.
* Automated monitoring.
* Trend discovery
