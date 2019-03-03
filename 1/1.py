import cv2

# загружаем изображение и отображаем его
image = cv2.imread("1.jpg")

# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

print("Введите угол поворота изображения в градусах")
angle = int(input())
# повернем изображение на заданный угол
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated image", rotated)

# запишем результирующее изображение на диск
cv2.imwrite("result.bmp", rotated)

#выход при нажатии на 0
cv2.waitKey(0)
