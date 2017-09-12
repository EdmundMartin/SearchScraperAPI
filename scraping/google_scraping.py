import asyncio

import aiohttp

from common.exceptions import *
from common.headers import random_desktop_headers
from common.google_urls import google_geos
from parsing.google_result_parser import parse_html


async def google_request(url, proxy):
    async with aiohttp.ClientSession() as client:
        try:
            async with client.get(url, headers=random_desktop_headers(), proxy=proxy, timeout=60) as response:
                html = await response.text()
                return {'html': html, 'status': response.status, 'error': None}
        except aiohttp.ClientError as err:
            return {'error': err}


def build_google_url(geo, keyword, number):
    keyword = keyword.replace(' ', '+')
    if geo:
        url = google_geos.get(geo, 'https://www.google.com/search?q={}&num={}&hl=en')
        return url.format(keyword, number)
    else:
        return 'https://www.google.com/search?q={}&num={}&hl=en'.format(keyword, number)


def unpack_data(data_dict):
    keyword, geo, number = data_dict.get('keyword'), data_dict.get('geo'), data_dict.get('number', '100')
    proxy = data_dict.get('proxy')
    if not keyword:
        raise NoKeywordProvided('No keyword was provided')
    if proxy:
        proxy = 'http://{}'.format(proxy)
    return keyword, geo, number, proxy


async def google_gather_results(data):
    result_dict = dict()
    try:
        keyword, geo, number, proxy = unpack_data(data)
        google_url = build_google_url(geo, keyword, number)
        html_result = await google_request(google_url, proxy)
        results = parse_html(html_result['html'])
        result_dict['results'] = results
        result_dict['keyword'] = keyword
        result_dict['geo'] = geo
        result_dict['error'] = None
        return result_dict
    except Exception as err:
        await asyncio.sleep(0)
        return {'error': str(err)}
