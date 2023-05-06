import requests
import base64
import json

import argparse


def request_txt2img(input, output_pre:str):
    response = requests.post(url=f'http://127.0.0.1:7861/sdapi/v1/img2img', json=payload)
    
    open('img2img_reponse.json', 'w').write(response.text)
    
    r = response.json()
    for key in r.keys():
        print(key)
    if 'detail' in r:
        print(r['detail'])

    i = 0
    for img_str in r['images']:
        image_base64_string = img_str
        # 将 base64 字符串解码成图片字节码
        image_data = base64.b64decode(image_base64_string)
        # 将字节码以二进制形式存入图片文件中，注意 'wb'
        with open(output_pre+f'{i}.png', 'wb') as jpg_file:
            jpg_file.write(image_data)
        i += 1 

parser = argparse.ArgumentParser(description="Crop transparent areas from an image.")
parser.add_argument("--input-json", required=True, help="Path to the input json.")
parser.add_argument("--input-img", required=True, help="Path to the input image.")
parser.add_argument("--output-pre", required=True, help="Path to save the cropped image.")

def decode_base64_to_image(encoding):
    from io import BytesIO
    from PIL import Image
    if encoding.startswith("data:image/"):
        encoding = encoding.split(";")[1].split(",")[1]
    try:
        image = Image.open(BytesIO(base64.b64decode(encoding)))
        image.save('base64img.png')
        return image
    except Exception as err:
        raise HTTPException(status_code=500, detail="Invalid encoded image")
    
if "__main__" == __name__:
    # 解析命令行参数
    args = parser.parse_args()
    with open(args.input_json, "r") as json_file:
        payload = json.load(json_file)

    input_file_path = args.input_img
    
    with open(input_file_path, 'rb') as f:
        import base64
        base64_bytes = base64.b64encode(f.read())
        s = str(base64_bytes, "utf-8")

        
        # print(s)
        payload["init_images"][0] = s

        [decode_base64_to_image(x) for x in payload["init_images"]]
        

        image_data = base64.b64decode(s)
        # 将字节码以二进制形式存入图片文件中，注意 'wb'
        with open('test.png', 'wb') as jpg_file:
            jpg_file.write(image_data)

    print(payload)
    request_txt2img(payload, args.output_pre)