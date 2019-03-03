import cv2
import math

# загружаем изображение и отображаем его
image = cv2.imread("1.jpg")

# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

print("Введите угол поворота изображения в градусах")
angle = int(input())
# повернем изображение на заданный угол
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated image", rotated)


print("Введите коэффициент изменения длины")
k = float(input())
print("Введите признак используемой интерполяционной схемы ( 0 – нулевого порядка, 1 – первого порядка, 2- третьего порядка).")
i = int(input())
if k > 0 and k <=1:
    s = 1/k
    dim = (int(w/k), int(h*s))

    if i == 0:
        result = cv2.resize(image, dim, interpolation = cv2.INTER_NEAREST)
    elif i == 1:
        result = cv2.resize(image, dim, interpolation = cv2.INTER_LINEAR)
    elif i == 2:
        result = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    else:
        print("Неправильно введен признак используемой интерполяционной схемы")
    cv2.imshow("Resize image", result)
    cv2.waitKey(0)

# запишем результирующее изображение на диск
    cv2.imwrite("result.bmp", result)
else:
    print("Коэффициент должен быть больше 0 и меньше или равен 1.")

cv2.destroyAllWindows()
