import requests
from pprint import pprint
response= requests.delete('https://jsonplaceholder.typicode.com/posts/1')
pprint(response.status_code)
pprint(response.text)
