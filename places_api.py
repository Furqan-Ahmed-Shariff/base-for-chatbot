import requests

url = "https://local-business-data.p.rapidapi.com/search-nearby"

querystring = {
    "query": "restauraunts",
    "lat": "37.359428",
    "lng": "-121.925337",
    "limit": "20",
    "language": "en",
    "region": "us",
}

headers = {
    "X-RapidAPI-Key": "58beedd836mshd1fe15a27542864p14f2bajsn039e4056366e",
    "X-RapidAPI-Host": "local-business-data.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
