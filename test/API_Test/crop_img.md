# 单张图片编辑



## 1. 去除背景图，保持背景透明

使用自定义的FastAPI,代码位于[api.py ](/modules/api.py)

```bash
python remove_bg_client.py --input out_img2img0.png --output nobg_img.png


```



## 2. 裁剪：

> 前提：裁剪的图片具有alpha通道



[纯客户端代码](crop_transparent.py)

使用说明:

```bash
python crop_transparent.py --input nobg_img.png --output croped.png
```

执行后生成的文件位于本地，

## 3. 扩展大小，并指定新位置

[纯客户端代码](expand_transparent.py)



使用说明:

```bash
python expand_transparent.py --input croped.png --output expand.png --input-json expand_config.json 
```



重要配置,来源与配置文件**expand_config.json**:

* size_w: 扩展目标宽度
* size_h: 扩展目标高度
* origin_x: 在新图像中的启示位置x
* origin_y: 在芯图像中的启示位置y