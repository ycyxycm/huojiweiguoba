from huojiweiguoba.lbw_pscript import RabbitMQ, PsdTask, ResultFormat, ScriptType

import base64
from PIL import Image
from io import BytesIO


def image_to_base64(image_path):
    """
    将图片转换为Base64编码。

    参数：
    image_path (str): 图片文件的路径

    返回：
    str: Base64编码的字符串
    """
    with open(image_path, "rb") as image_file:
        # 读取图片内容
        image_data = image_file.read()
        # 将图片内容转换为Base64编码
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
        return base64_encoded


def base64_to_image(base64_string):
    """
    将Base64编码转换为图片。

    参数：
    base64_string (str): Base64编码的字符串

    返回：
    PIL.Image.Image: 图片对象
    """
    # 解码Base64字符串
    image_data = base64.b64decode(base64_string)
    # 将二进制数据转换为图片对象
    image = Image.open(BytesIO(image_data))
    return image


if __name__ == "__main__":

    # stamp_items = {
    #     "搞怪笑脸_K": {
    #         "搞怪笑脸_K_": "/Users/hwj/工作/ps-project/rabbitmq/短裤-冰丝四面弹短裤/印花已完成20240307175543/搞怪笑脸_K_/搞怪笑脸_K_.png"
    #     },
    #     "生命力_K": {
    #         "生命力_K_": "/Users/hwj/工作/ps-project/rabbitmq/短裤-冰丝四面弹短裤/印花已完成20240307175543/生命力_K_/生命力_K_.png"
    #     }
    # }
    # template_items = {
    #     "卡其": "/Users/hwj/工作/ps-project/rabbitmq/短裤-冰丝四面弹短裤/卡其.psd",
    #     "深灰": "/Users/hwj/工作/ps-project/rabbitmq/短裤-冰丝四面弹短裤/深灰.psd",
    #     "黑色": "/Users/hwj/工作/ps-project/rabbitmq/短裤-冰丝四面弹短裤/黑色.psd"
    # }
    # # 本地图片转为二进制
    # stamp_items1 = {}
    # for x, y in stamp_items.items():
    #     if x not in stamp_items1.keys(): stamp_items1[x] = {}
    #     for k1, v1 in y.items():
    #         stamp_items1[x].__setitem__(k1, open(v1, 'rb').read())
    #         # stamp_items1[x].__setitem__(k1, image_to_base64(v1))
    # template_items = {k: open(v, 'rb').read() for k, v in template_items.items()}
    # # template_items = {k: image_to_base64(v) for k, v in template_items.items()}
    # print(stamp_items1)
    # pt = PsdTask(
    #     script_type=ScriptType.single,
    #     result_format=ResultFormat.listing,
    #     stamp_items=stamp_items1,
    #     template_items=template_items,
    #     name="批次1",
    #     uname="卢本伟"
    # )
    rabbitmq1 = RabbitMQ("卢本伟9")
    rabbitmq1.on_line()
    # print(len(rabbitmq1.get_queue_info()))
    # print(rabbitmq1.get_queue_running_info())

    # rabbitmq1.publish(pt)

    # rabbitmq = RabbitMQ("卢本伟1号")
    # rabbitmq.consume(ifunc)

    # rabbitmq = RabbitMQ("卢本伟2号")
    # rabbitmq.consume(ifunc)
