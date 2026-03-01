from PIL import Image
import requests


# This code demonstrates how to handle binary responses from HTTP requests. It fetches an image from the web, saves it locally, and then opens it using the PIL library.
response = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/640px-PNG_transparency_demonstration_1.png")
with open("image.png", "wb") as f:
    f.write(response.content)
img = Image.open("image.png")
img.show()
