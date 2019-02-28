import asyncio

import aiohttp

from searchscrapeserver.common.exceptions import *
from searchscrapeserver.common.headers import random_desktop_headers
from searchscrapeserver.common.yandex_urls import yandex_geos
from searchscrapeserver.parsing.yandex_result_parser import parse_html
from searchscrapeserver.scraping.requests import get_request


DEFAULT_YANDEX_URL = 'https://yandex.com/search/?text={}&lr={}&numdoc={}'


def build_yandex_url(geo, keyword, number, lr):
    keyword = keyword.replace(' ', '+')
    if geo:
        url = yandex_geos.get(geo, DEFAULT_YANDEX_URL)
        return url.format(keyword, lr, number)
    else:
        return DEFAULT_YANDEX_URL.format(keyword, lr, number)


def unpack_data(data_dict):
    keyword, geo, number = data_dict.get('keyword'), data_dict.get('geo'), data_dict.get('number', '100')
    lr = data_dict.get('lr', '10394')
    proxy = data_dict.get('proxy')
    if not keyword:
        raise NoKeywordProvided('No keyword was provided')
    if proxy:
        proxy = 'http://{}'.format(proxy)
    return keyword, geo, number, lr,  proxy


async def yandex_gather_results(data):
    result_dict = dict()
    keyword, geo, number, lr, proxy = unpack_data(data)
    try:
        google_url = build_yandex_url(geo, keyword, number, lr)
        html_result = await get_request(google_url, proxy)
        if html_result.get('error'):
            return {'keyword': keyword, 'geo': geo, 'proxy': proxy, 'error': 'Client error - likely connectivity issue'}
        if html_result.get('status') > 499:
            return {'keyword': keyword, 'geo': geo, 'proxy': proxy, 'error': 'Request rejected by Yandex'}
        results = parse_html(html_result['html'])
        result_dict['results'] = results
        result_dict['keyword'] = keyword
        result_dict['geo'] = geo
        return result_dict
    except Exception as err:
        await asyncio.sleep(0)
        return {'error': str(err), 'keyword': keyword, 'geo': geo, 'proxy': proxy}
