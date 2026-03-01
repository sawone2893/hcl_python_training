import requests
from pprint import pprint
#redirects to https://mail.google.com/mail/
response =requests.get('https://www.gmail.com')
pprint(response.history)

#timeout after 1 second
try:    
    response = requests.get('https://www.gmail.com', timeout=.1)
    print(response.status_code)
except requests.exceptions.Timeout:
    print('The request timed out')