import requests
from pprint import pprint
import webbrowser
url="https://pastebin.com/api/api_post.php"
data={
    "api_dev_key":"yQ4jUBv7GLGMdvowd4IFdJJWUDHopwsW",
    "api_option":"paste",
    "api_paste_code":"print('Hello, World!')",
    "api_paste_name":"HelloWorld.py",
    "api_paste_private":"1",
    "api_paste_expire_date":"10M"
}
response=requests.post(url,data=data)
pprint(response.text)
webbrowser.open(response.text)

