import requests
from pprint import pprint
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get("https://swapi.dev/api/people/1/", headers=headers)
pprint(response.headers)
pprint(response.headers['Content-Type'])
pprint(response.request.headers)

