import argparse
from .utils import _determine_handlers, _get_site_name

from .show import Show
from .episode import Episode



def fetch_ratings(show_url, handlers):
    ratings = {}
    for handler in handlers:
        site_name = handler.site_name
        ratings[site_name] = handler.get_show_ratings(show_url)

    return ratings

def main():
    # -l --link
    arg_parser = argparse.ArgumentParser(description='')
    arg_parser.add_argument('-l', '--link', type=str, help='Link to download')
    arg_parser.add_argument('-o', '--output', type=str, help='Output file name')

    args = arg_parser.parse_args()

    site_links = args.link.split(',')
    handlers = _determine_handlers(site_links)

    if handlers is []:
        print('Handler not found')
        return
    

    ratings = fetch_ratings(args.link, handlers)

    return ratings

if __name__ == '__main__':
    main()