from .base_site import BaseSite
from .request_utils import _make_request
from bs4 import BeautifulSoup
import re
import json

EPISODES_SLUG = "/episodes/"
IMDB_BASE_URL = "https://www.imdb.com/"

HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.6',
  'cache-control': 'max-age=0',
  'priority': 'u=0, i',
  'referer': 'https://www.imdb.com/title/tt0903747/?ref_=ttep_ov',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

class IMDb(BaseSite):
    def __init__(self):
        self.site_name = "IMDb"
        
    def get_all_season_urls(self, show_url):
        response = _make_request(show_url + EPISODES_SLUG, headers=HEADERS)

        soup = BeautifulSoup(response, 'html.parser')

        # extract all data-testid="tab-season-entry" href links
        season_urls = []
        for a_tag in soup.find_all('a', {'data-testid': 'tab-season-entry'}):
            href = a_tag.get('href')
            if href:
                season_urls.append(IMDB_BASE_URL + href)

        return season_urls

    def get_specific_season_ratings(self, season_url):
        response = _make_request(season_url, headers=HEADERS)

        try:
            # Extract the JSON data from the script tag with id="__NEXT_DATA__" where all the ratings are stored
            # TODO Should probably not be using regex to parse HTML :D
            json_data = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', response).group(1)
            
            # Parse the JSON data
            data = json.loads(json_data)
            
            # Navigate through the JSON structure to find the aggregate rating
            try:
                season_info = data['props']['pageProps']['contentData']['section']['episodes']['items']
            except KeyError:
                print("Could not find season info")
                return None
            
            # go throughh each item in _json and extract the rating
            ratings = {}
            for episode_num, episode_rating in enumerate(season_info, start=1):
                ratings[episode_num] = episode_rating['aggregateRating']

            return ratings

        except (AttributeError, KeyError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to extract ratings from {season_url} due to {e}")


    def get_show_ratings(self, show_url):
        all_season_urls = self.get_all_season_urls(show_url)

        ratings = {}
        for season_num, season_url in enumerate(all_season_urls, start=1):
            ratings[season_num] = self.get_specific_season_ratings(season_url)
        
        return ratings