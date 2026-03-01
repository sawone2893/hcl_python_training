import requests
from pprint import pprint
# The response format is determined by the server and is indicated in the Content-Type header of the response.
response = requests.get("https://jsonplaceholder.typicode.com/posts/1", params={"userId": 1})
print(response.status_code)
contentType=response.headers["Content-Type"]
if contentType == "application/json; charset=utf-8":
    pprint(response.json())
elif contentType == "text/html; charset=utf-8":
    print(response.text)

# In this example, we make a GET request to a URL that returns a JSON response. We check the Content-Type header to determine the format of the response and then parse it accordingly. If the response is in JSON format, we use the .json() method to parse it into a Python dictionary. If it's in HTML format, we simply print the text content of the response.