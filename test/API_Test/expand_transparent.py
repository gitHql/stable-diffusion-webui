from PIL import Image

def expand_image(input_file_path: str, output_file_path: str, start_coord: tuple, window_size: tuple):
    # 打开裁剪好的图片文件
    cropped_image = Image.open(input_file_path)

    # 创建一个与整个窗口尺寸相同的透明背景图像
    expanded_image = Image.new("RGBA", window_size, (255, 255, 255, 0))

    # 将裁剪好的图片粘贴到指定的起始坐标
    expanded_image.paste(cropped_image, start_coord)

    # 保存扩充边缘后的图片
    expanded_image.save(output_file_path)

import argparse
parser = argparse.ArgumentParser(description="Crop transparent areas from an image.")
parser.add_argument("--input", required=True, help="Path to the input image.")
parser.add_argument("--output", required=True, help="Path to save the cropped image.")
parser.add_argument("--input-json", required=True, help="Path to the input image.")

if __name__ == "__main__":
    # 解析命令行参数
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output
    with open(args.input_json, "r") as json_file:
        import json
        js = json.load(json_file)

    start_coord = (js['origin_x'], js['origin_y'])  # 指定起始坐标，例如：(50, 50)
    window_size = (js['size_w'], js['size_h'])  # 指定整个窗口的尺寸，例如：(500, 500)
    expand_image(input_file_path, output_file_path, start_coord, window_size)
    print(f"Expanded image saved to {output_file_path}")
