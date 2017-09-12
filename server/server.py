import asyncio

from aiohttp import web

from scraping.google_scraping import google_gather_results
from scraping.bing_scraping import bing_gather_results


class GoogleScraperServer:

    def __init__(self):

        self.loop = asyncio.get_event_loop()

    async def scrape_google_single_keyword(self, request):
        data = await request.json()
        results = await google_gather_results(data)
        return web.Response(text=str(results))

    async def scrape_google_multiple_keywords(self, request):
        response = dict()
        results = []
        data = await request.json()
        queries = data.get('queries')
        tasks = [google_gather_results(query) for query in queries]
        for result in asyncio.gather(*tasks):
            results.append(result)
        response['queries'] = results
        return web.Response(text=str(response))

    async def scrape_bing_single_keyword(self, request):
        data = await request.json()
        results = await bing_gather_results(data)
        return web.Response(text=str(results))

    def run_server(self):
        app = web.Application(loop=self.loop)
        app.router.add_post('/google-single-keyword', self.scrape_google_single_keyword)
        app.router.add_post('/google-multiple-keywords', self.scrape_google_multiple_keywords)
        app.router.add_post('/bing-single-keyword', self.scrape_bing_single_keyword)
        web.run_app(app, host='127.0.0.1', port=8080)