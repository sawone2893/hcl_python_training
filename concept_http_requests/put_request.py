import requests
from pprint import pprint
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data={'title': 'foo'})
print(response.status_code)
pprint(response.json())
