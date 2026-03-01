import requests
from pprint import pprint
from requests import exceptions

try:response = requests.get('https://nonexistentwebsite.com') 
except exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')

try:response = requests.get('https://httpbin.org/status/404')
except exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

try:response = requests.get('https://httpbin.org/delay/5', timeout=2)
except exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')

try:response = requests.get('https://httpbin.org/get')
except exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')