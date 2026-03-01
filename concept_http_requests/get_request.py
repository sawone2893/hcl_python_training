import requests
from pprint import pprint   
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
pprint(response.json())