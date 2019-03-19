from bs4 import BeautifulSoup
import requests
import urls


def request_url(site, uri):
    res = requests.get(site)
    soup = BeautifulSoup(res.text, 'html.parser')
    uri = uri
    url = soup.select_one(uri)
    result = url.get('src')

    iframe = urls.urljoin(urls.getHostname(site, True), result)

    print (iframe)
    return iframe


def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)

