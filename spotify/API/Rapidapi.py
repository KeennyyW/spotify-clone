import requests



def artist_data():
    

    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/overview"

    querystring = {"artistId":"6eUKZXaKkcviH0Ku9w2n3V"}

    headers = {
        "x-rapidapi-key": "cc49d36267msh050e72f34e20be7p1bd57djsne18bef43adb2",
        "x-rapidapi-host": "spotify-scraper.p.rapidapi.com"
    }

    response_api = requests.get(url, headers=headers, params=querystring)

    response = response_api.json()

    return response

response = artist_data()