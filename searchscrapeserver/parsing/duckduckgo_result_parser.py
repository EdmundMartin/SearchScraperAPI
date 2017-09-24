from lxml import html as lh
from bs4 import BeautifulSoup


def parse_html(html):
    results = []
    lxml_doc = lh.fromstring(html)
    result_blocks = lxml_doc.cssselect('div#links div.result__body')
    rank = 1
    for res in result_blocks:
        result = attributes(res)
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

    description = soup.find('div', {'class':'result__snippet'})
    if description:
        description = description.get_text()

    return {'url': link, 'title': title, 'description': description}