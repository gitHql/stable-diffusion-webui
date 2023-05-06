import requests
import base64

IMAGE_NAME = 'rm_ret'

def send_request(input_file_path: str, output_file_path:str) -> dict:
    url = "http://localhost:7861/sdapi/v1/remove-bg"

    with open(input_file_path, "rb") as file:
        files = {"file": (input_file_path, file, "image/png")}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        json_ret = response.json()
        image_data = base64.b64decode(json_ret['image'])
        # 将字节码以二进制形式存入图片文件中，注意 'wb'
        with open(output_file_path, 'wb') as jpg_file:
            jpg_file.write(image_data)
            
        return json_ret
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

import argparse
parser = argparse.ArgumentParser(description="Crop transparent areas from an image.")
parser.add_argument("--input", required=True, help="Path to the input image.")
parser.add_argument("--output", required=True, help="Path to save the cropped image.")

if __name__ == "__main__":
    
    # 解析命令行参数
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output
    result = send_request(input_file_path, output_file_path)
    print(result)
