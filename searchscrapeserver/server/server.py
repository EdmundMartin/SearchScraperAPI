import asyncio
from typing import List
from urllib.parse import urlparse

from aiohttp import web
from searchit import YandexScraper, BingScraper, GoogleScraper, ScrapeRequest
from searchit.scrapers.qwant import QwantScraper
from searchit.scrapers import SearchResult
from marshmallow.exceptions import ValidationError

from searchscrapeserver.schemas.schemas import ScrapeItem


class SearchScraper:

    def __init__(self, host, port):

        try:
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        except ImportError:
            pass
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.schema = ScrapeItem()
        self._klasses = {
            'google': GoogleScraper, 'yandex': YandexScraper, 'bing': BingScraper, 'qwant': QwantScraper
        }

    def parse_url(self, url: str):
        return self._klasses[urlparse(url).path.lstrip('/').split('-')[0]]

    def _results_to_json(self, results: List[SearchResult]):
        json_result = []
        for result in results:
            json_result.append({
                "url": result.url,
                "title": result.title,
                "description": result.description,
                "rank": result.rank
            })
        return {"results": json_result}
    
    async def do_standard_req(self, request: web.Request):
        data = await request.json()
        try:
            input_data = self.schema.load(data)
        except ValidationError as e:
            return web.json_response(e.messages, status=400)
        klass = self.parse_url(str(request.url))
        request = ScrapeRequest(
            input_data["keyword"],
            input_data["number"],
            domain=input_data.get('domain'),
            proxy=input_data.get('proxy'),
            sleep=input_data.get('sleep', 0)
        )
        try:
            results = await klass().scrape(request)
            results = self._results_to_json(results)
        except Exception as e:
            return web.json_response({
                "errors": str(e)
            }, status=500)
        else:
            return web.json_response(results, status=200)

    async def scrape_single_keyword(self, request: web.Request):
        return await self.do_standard_req(request)

    def run_server(self):
        app = web.Application()
        app.router.add_post('/google-scrape', self.scrape_single_keyword)
        app.router.add_post('/bing-scrape', self.scrape_single_keyword)
        app.router.add_post('/yandex-scrape', self.scrape_single_keyword)
        app.router.add_post('/qwant-scrape', self.scrape_single_keyword)
        web.run_app(app, host=self.host, port=self.port)
