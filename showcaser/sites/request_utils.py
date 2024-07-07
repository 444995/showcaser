import requests

def _make_request(url, headers):
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to make request to {url}")