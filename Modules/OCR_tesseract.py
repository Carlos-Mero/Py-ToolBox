"""灵感和部分代码来源于博主「不会飞的渡渡鸟」https://blog.csdn.net/github_40102642/article/details/10592583
                   博主「Lewishoy」   https://blog.csdn.net/weixin_44911091/article/details/107936065
                   博主「Eastmount」  https://github.com/eastmountyxz/ImageProcessing-Python"""

import numpy as np
import cv2
import pytesseract
import os

# tesseract 的中文语言包
tessdata_path = os.path.abspath('Tesseract_OCR\\tessdata')
pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
os.environ['TESSDATA_PREFIX'] = tessdata_path
a = []  # 两个空的列表，用于这个函数的储存数据
b = []


def order_points(pts):  # 使用户输入的坐标得到一个简单的顺序，防止选区图片扭曲，也使得下一步的透视变换可以进行
    # 创建一个空的数组用于储存数据
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)  # 计算四个坐标的（x+y），将最大的置于0位（左上角），最小的坐标置于2位（右下角）
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)  # 计算四个坐标的|x-y|，将最大的置于3位（左下角），最小的坐标置于1位（右上角）
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


def perspective_transform(image, pts):  # 核心、透视变换函数
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # 重新计算新的图像的宽度和高度
    width1 = np.sqrt(np.sum((br - bl) ** 2))
    width2 = np.sqrt(np.sum((tr - tl) ** 2))
    max_width = max(int(width1), int(width2))
    height1 = np.sqrt(np.sum((tr - br) ** 2))
    height2 = np.sqrt(np.sum((tl - bl) ** 2))
    max_height = max(int(height1), int(height2))
    # 重新定义新的图像的四边顶点的坐标
    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")
    # 计算透视矩阵，并且变化应用
    m = cv2.getPerspectiveTransform(rect, dst)
    #print(m)  # 这里一直报错，测试用
    warped = cv2.warpPerspective(image, m, (max_width, max_height))
    return warped


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        a.append(x)  # 利用a来暂时储存横坐标
        b.append(y)  # 利用b来暂时储存纵坐标
        cv2.circle(img, (x, y), 3, (255, 0, 0), thickness=-1)  # 这里的目的是让单击后有一个反馈
        cv2.imshow("image", img)


def clahe(image):
    b, g, r = cv2.split(image)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)
    image_clahe = cv2.merge([b, g, r])
    return image_clahe


def main(path):  # 主函数
    global img  # 全局变量
    img = cv2.imread(path, -1)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    #cv2.imshow("image", img)  # 展示原始图片以建立选取
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    k0 = (a[0], b[0])  # 从暂存的数据中分配生成四个点的坐标
    k1 = (a[1], b[1])
    k2 = (a[2], b[2])
    k3 = (a[3], b[3])
    pts = np.array([k0, k1, k2, k3], dtype="float32")
    # 使用坐标完成鸟瞰的图像变化，这里的pts里的坐标，最好就是我们输入图像的四边顶点的坐标
    warped = perspective_transform(img, pts)
    #cv2.imshow("Warped", warped)  # 生成透视后的图片，单纯测试用，可屏蔽
    cv2.waitKey(0)
    im = warped
    #result = clahe(im)
    #cv2.imshow("result", result)  # 测试用，可屏蔽
    cv2.waitKey(0)
    # 4、输出结果，结束
    #text_eng = pytesseract.image_to_string(result, lang='eng')
    text_chi = pytesseract.image_to_string(im, lang='chi_sim')  # 利用pytesseract的内置函数，比较简单
    print(text_chi)


if __name__ == '__main__':
    main('~/Desktop/IMG_1008.JPG')
    # 这里是输入我自己测试图片，实际上输入路径即可
