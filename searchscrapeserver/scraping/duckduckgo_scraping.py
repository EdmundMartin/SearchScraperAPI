import asyncio

import aiohttp

from searchscrapeserver.common.exceptions import *
from searchscrapeserver.common.headers import random_desktop_headers
from searchscrapeserver.parsing.duckduckgo_result_parser import parse_html


DEFAULT_DDG_URL = 'https://duckduckgo.com/html/?q={}'

async def ddg_request(url, proxy):
    async with aiohttp.ClientSession() as client:
        try:
            async with client.get(url, headers=random_desktop_headers(), proxy=proxy, timeout=60) as response:
                html = await response.text()
                return {'html': html, 'status': response.status}
        except aiohttp.ClientError as err:
            return {'error': err}


def build_ddg_url(keyword):
    return DEFAULT_DDG_URL.format(keyword.replace(' ', '+'))


def unpack_data(data_dict):
    keyword, geo, number = data_dict.get('keyword'), data_dict.get('geo'), data_dict.get('number', '100')
    proxy = data_dict.get('proxy')
    if not keyword:
        raise NoKeywordProvided('No keyword was provided')
    if proxy:
        proxy = 'http://{}'.format(proxy)
    return keyword, geo, number, proxy


async def ddg_gather_results(data):
    result_dict = dict()
    keyword, geo, number, proxy = unpack_data(data)
    try:
        ddg_url = build_ddg_url(keyword)
        html_result = await ddg_request(ddg_url, proxy)
        if html_result.get('error'):
            return {'keyword': keyword, 'geo': geo, 'proxy': proxy, 'error': 'Client error - likely connectivity issue'}
        if html_result.get('status') > 499:
            return {'keyword': keyword, 'geo': geo, 'proxy': proxy, 'error': 'Request rejected by Google'}
        results = parse_html(html_result['html'])
        result_dict['results'] = results
        result_dict['keyword'] = keyword
        result_dict['geo'] = geo
        return result_dict
    except Exception as err:
        await asyncio.sleep(0)
        return {'error': str(err), 'keyword': keyword, 'geo': geo, 'proxy': proxy}