from sys import argv
import base64
import json
# 从命令行获得文件名参数
SCRIPT_NAME, JSON_NAME, IMAGE_NAME = argv
# 读取 json 文件，并直接存入字典
with open(JSON_NAME, "r") as json_file:
    raw_data = json.load(json_file)
# 从字典中取得图片的 base64 字符串，形如“YABgAAD/2wBDAAYEBQYFBAY...."，
image_base64_string = raw_data["images"][0]
# 将 base64 字符串解码成图片字节码
image_data = base64.b64decode(image_base64_string)
# 将字节码以二进制形式存入图片文件中，注意 'wb'
with open(IMAGE_NAME, 'wb') as jpg_file:
    jpg_file.write(image_data)