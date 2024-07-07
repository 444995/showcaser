from urllib.parse import urlparse
from .sites import imdb


def _get_site_name(url):
    return urlparse(url).netloc

def _determine_handlers(urls):
    handlers = []
    for url in urls:
        if _get_site_name(url) == 'www.imdb.com':
            handlers.append(imdb.IMDb())
        
    return handlers

