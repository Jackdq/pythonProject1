import cv2

# 读取图像
im = cv2.imread('test.jpg')
h, w = im.shape[:2]
assert isinstance(w, object)
print(h, w)
