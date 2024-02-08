
import base64
import os
import re

import cv2
import numpy as np
import pytesseract


#抽取信息的函数
def extract_information(text):
    lines = text.split('\n')

    # extract the first line (name)
    name = lines[0].replace(" ", "")

    # extract the identity card number
    id_number_line = lines[-3]
    id_number = re.search(r'(\d{18}|\d{17}[xX])', id_number_line)
    id_number = id_number.group(1) if id_number else ""

    # create a mapper (dictionary)
    mapper = {"name": name, "ID": id_number}

    return mapper

#调用识别和预处理图像代码的函数
def extract_id_info(image_base64):
    # 设置TESSDATA_PREFIX环境变量，指向tessdata文件夹所在的路径
    os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

    # 设置Tesseract OCR的路径
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # 读取身份证图片
    # 将 base64 编码转换成 OpenCV 图像
    img = base64_to_cv2(image_base64)
    # img = cv2.imread(image_path)
    # 显示图像
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 将图片转换为灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, lang='chi_sim+eng')



    return extract_information(text)

def base64_to_cv2(base64_string):
    # 去掉 base64 编码字符串的头部信息
    base64_string = base64_string.split(',')[1]

    # 将 base64 编码字符串解码为图像数据
    decoded_data = base64.b64decode(base64_string)

    # 将解码后的数据转换成 numpy 数组
    np_data = np.frombuffer(decoded_data, np.uint8)

    # 将 numpy 数组转换成 OpenCV 图像
    image = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    return image
