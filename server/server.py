import asyncio

from aiohttp import web

from scraping.google_scraping import google_gather_results
from scraping.bing_scraping import bing_gather_results
from schemas.google_schemas import GoogleSingleItem

class SearchScraper:

    def __init__(self):

        self.loop = asyncio.get_event_loop()
        self.google_schema = GoogleSingleItem()

    async def scrape_google_single_keyword(self, request):
        data = await request.json()
        input_data, errors = self.google_schema.load(data)
        if errors:
            return web.json_response(errors, status=400)
        results = await google_gather_results(input_data)
        return web.json_response(results, status=200)

    async def scrape_bing_single_keyword(self, request):
        data = await request.json()
        results = await bing_gather_results(data)
        return web.json_response(results, status=200)

    def run_server(self):
        app = web.Application(loop=self.loop)
        app.router.add_post('/google-scrape', self.scrape_google_single_keyword)
        app.router.add_post('/bing-single-keyword', self.scrape_bing_single_keyword)
        web.run_app(app, host='127.0.0.1', port=8080)