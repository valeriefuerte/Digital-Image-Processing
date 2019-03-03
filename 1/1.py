import cv2

# загружаем изображение и отображаем его
image = cv2.imread("1.jpg")
#cv2.imshow("Original image", image)
#cv2.waitKey(0)

# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

print("Введите угол поворота изображения в градусах")
angle = int(input())
# повернем изображение на 180 градусов
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)
