import requests
from pprint import pprint
response = requests.get("https://jsonplaceholder.typicode.com/posts/1212312")
pprint(response.status_code)
if response.status_code == 200:
    pprint(response.json())
else:    print("An error occurred while fetching the data.")
