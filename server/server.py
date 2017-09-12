import asyncio

from aiohttp import web

from scraping.google_scraping import gather_results


class GoogleScraperServer:

    def __init__(self):

        self.loop = asyncio.get_event_loop()

    async def scrape_google_single_keyword(self, request):
        data = await request.json()
        results = await gather_results(data)
        return web.Response(text=str(results))

    async def scrape_google_multiple_keywords(self, request):
        response = dict()
        results = []
        data = await request.json()
        queries = data.get('queries')
        tasks = [gather_results(query) for query in queries]
        for result in asyncio.gather(*tasks):
            results.append(result)
        response['queries'] = results
        return web.Response(text=str(response))

    def run_server(self):
        app = web.Application(loop=self.loop)
        app.router.add_post('/google-single-keyword', self.scrape_google_single_keyword)
        app.router.add_post('/google-multiple-keywords', self.scrape_google_multiple_keywords)
        web.run_app(app, host='127.0.0.1', port=8080)