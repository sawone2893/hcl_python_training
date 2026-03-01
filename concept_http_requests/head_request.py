import requests
from pprint import pprint
import json
response= requests.head('https://www.example.com')
print(response.status_code)
#print(response.headers)
res_headers = response.headers
print(res_headers['Content-Type'])
print(res_headers['Age'])
