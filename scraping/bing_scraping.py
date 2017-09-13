import asyncio

import aiohttp

from common.exceptions import *
from common.headers import random_desktop_headers
from common.bing_urls import bing_geos
from parsing.bing_result_parser import parse_html


async def bing_request(url, proxy):
    async with aiohttp.ClientSession() as client:
        try:
            async with client.get(url, headers=random_desktop_headers(), proxy=proxy, timeout=60) as response:
                html = await response.text()
                return {'html': html, 'status': response.status, 'error': None}
        except aiohttp.ClientError as err:
            return {'error': err}


def build_bing_url(geo, keyword, number):
    keyword = keyword.replace(' ', '+')
    if geo:
        url = bing_geos.get(geo, 'http://www.bing.com/search?q={}&count={}')
        return url.format(keyword, number)
    else:
        return 'http://www.bing.com/search?q={}&count={}'.format(keyword, number)


def unpack_data(data_dict):
    keyword, geo, number = data_dict.get('keyword'), data_dict.get('geo'), data_dict.get('number', 50)
    proxy = data_dict.get('proxy')
    if not keyword:
        raise NoKeywordProvided('No keyword was provided')
    if proxy:
        proxy = 'http://{}'.format(proxy)
    return keyword, geo, number, proxy


async def bing_gather_results(data):
    result_dict = dict()
    keyword, geo, number, proxy = unpack_data(data)
    try:
        bing_url = build_bing_url(geo, keyword, number)
        html_result = await bing_request(bing_url, proxy)
        results = parse_html(html_result['html'])
        result_dict['results'] = results
        result_dict['keyword'] = keyword
        result_dict['geo'] = geo
        return result_dict
    except Exception as err:
        await asyncio.sleep(0)
        return {'error': str(err), 'keyword': keyword, 'geo': geo, 'proxy': proxy}
