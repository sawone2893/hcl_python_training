import requests
from pprint import pprint
response = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': 'foo', 'body': 'bar', 'userId': 1})
print(response.status_code)
print(response.headers['Content-Type'])
print(response.text)
print(response.json())
pprint(response.json())
# Output:
# 201
# application/json; charset=utf-8