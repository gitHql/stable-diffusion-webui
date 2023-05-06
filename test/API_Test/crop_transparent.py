from PIL import Image

from PIL import Image, ImageChops

def crop_transparent(input_file_path: str, output_file_path: str, alpha_threshold: int = 30):
    # 打开图片文件
    image = Image.open(input_file_path)

    # 获取图片的透明度通道
    alpha = image.split()[3]

    # 将alpha通道中的值小于阈值的像素设置为完全透明
    alpha = alpha.point(lambda p: p > alpha_threshold and 255)

    # 使用修改后的alpha通道创建新的RGBA图像
    image = Image.merge("RGBA", image.split()[:3] + (alpha,))

    # 创建一个与原图大小相同的透明背景图像
    background = Image.new("RGBA", image.size, (255, 255, 255, 0))

    # 计算背景与原图的差异区域
    diff = ImageChops.difference(image, background)

    # 从差异区域获取边界框
    bbox = diff.getbbox()

    # 使用边界框裁剪图片
    cropped_image = image.crop(bbox)

    # 保存裁剪后的图片
    cropped_image.save(output_file_path)



import argparse
parser = argparse.ArgumentParser(description="Crop transparent areas from an image.")
parser.add_argument("--input", required=True, help="Path to the input image.")
parser.add_argument("--output", required=True, help="Path to save the cropped image.")

if __name__ == "__main__":
    # 解析命令行参数
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output
    crop_transparent(input_file_path, output_file_path)
    print(f"Cropped image saved to {output_file_path}")
