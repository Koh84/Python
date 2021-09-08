import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png")
print("Status code:", r.status_code)
image = Image.open(BytesIO(r.content))
print("image info:", image.size, image.format, image.mode)
path = "./image."+image.format

try:
    image.save(path, image.format)
except IOError:
    print("Can't save image")
