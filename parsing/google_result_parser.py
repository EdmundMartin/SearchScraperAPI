from lxml import html as lh
from bs4 import BeautifulSoup

def parse_html(html):
    results = []
    lxml_doc = lh.fromstring(html)
    result_blocks = lxml_doc.cssselect('div.g')
    rank = 1
    for res in result_blocks[:-1]:
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

    title = soup.find('h3', {'class':'r'})
    if title:
        title = title.get_text()

    description = soup.find('span', {'class':'st'})
    if description:
        description = description.get_text()

    return {'url': link, 'title': title, 'description': description}