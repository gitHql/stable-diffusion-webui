import requests
import base64
import json
from sys import argv

SCRIPT_NAME, JSON_NAME, IMAGE_NAME = argv

with open(JSON_NAME, "r") as json_file:
    payload = json.load(json_file)

response = requests.post(url=f'http://127.0.0.1:7861/sdapi/v1/txt2img', json=payload)
r = response.json()
open('reponse.json', 'w').write(response.text)
i = 0
for img_str in r['images']:
    image_base64_string = img_str
    # 将 base64 字符串解码成图片字节码
    image_data = base64.b64decode(image_base64_string)
    # 将字节码以二进制形式存入图片文件中，注意 'wb'
    with open(IMAGE_NAME+f'{i}.png', 'wb') as jpg_file:
        jpg_file.write(image_data)
    i += 1 