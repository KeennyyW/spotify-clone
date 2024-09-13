import requests
from music.utils import artist_uri_to_id


def artist_data():
    

    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/overview"

    artist_id = artist_uri_to_id()

    querystring = {"artistId":artist_id}

    headers = {
        "x-rapidapi-key": "cc49d36267msh050e72f34e20be7p1bd57djsne18bef43adb2",
        "x-rapidapi-host": "spotify-scraper.p.rapidapi.com"
    }

    response_api = requests.get(url, headers=headers, params=querystring)

    response_data = response_api.json()

    artist_info = []

    biography = response_data.get('biography')
    banner = response_data.get('visuals', {}).get('header',[{}])[0].get('url')

    artist_info.append((biography, banner))


    return artist_info

#artist_data()