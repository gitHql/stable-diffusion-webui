# img2img 

[参数文件](img2img.json)



## 功能说明

通过初始化图片和描述语言进一步生成相似图片。



## 核心参数

* "prompt": "",
* "negative_prompt":
* "initial_noise_multiplier": 1,  **这个参数不能为0，否则导致生成的图片是空白**
*   "sampler_name": "DPM++ 2M Karras",
     "sampler_index": "DPM++ 2M Karras",

* "init_images": [
          ""
      ], **这个参数通过代码中进一步修改，配置文件设置为空字符串**

## 脚本命令：

```bash
python request_img2img_v1.py --input-json img2img.json --input-img out_img2img0.png --output out_img2img
```

