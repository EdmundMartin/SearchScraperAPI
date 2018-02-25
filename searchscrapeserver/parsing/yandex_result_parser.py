from lxml import html as lh
from bs4 import BeautifulSoup
import re

def parse_html(html):
    results = []
    lxml_doc = lh.fromstring(html)
    result_blocks = lxml_doc.cssselect('li.serp-item')
    rank = 1
    for res in result_blocks:
        result = attributes(res)
        if result:
            result.update({'rank': rank})
            results.append(result)
            rank += 1
    return results


def attributes(result_block):
    html = lh.tostring(result_block).decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')

    link = soup.find('a', href=True)
    if link:
        link = link['href']

    title = soup.find('h2')
    if title:
        title = title.get_text()
        title = re.sub('^\d+', '', title).lstrip(' ')

    description = soup.find('div', {'class': 'organic__content-wrapper'})
    if description:
        description = description.get_text()

    if not link.startswith('//'):
        return {'url': link, 'title': title, 'description': description}
    else:
        return None