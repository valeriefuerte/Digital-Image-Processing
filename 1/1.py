import cv2
import numpy as np

# загружаем изображение и отображаем его
image = cv2.imread("1.jpg")

# получим размеры изображения для поворота
# и вычислим центр изображения
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

print("Введите угол поворота изображения в градусах")
angle = int(input())%360
# повернем изображение на заданный угол
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, 1.0)
#найдем новые размеры изображения
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
tg = sin / cos

new_w = int((h * sin) + (w * cos))
new_h = int((h * cos) + (w * sin))

M[0, 2] += (new_w / 2) - center[0]
M[1, 2] += (new_h / 2) - center[1]

rotated = cv2.warpAffine(image, M, (new_w, new_h))
#cv2.imshow("Rotated image", rotated)
#cv2.waitKey(0)

#обрежем до прямоугольника
h_sin = int(h * sin)
h, w, _ = rotated.shape
row_1 = int((w - 2 * h_sin) * tg)
row_2 = h - int((w - 2 * h_sin) * tg)
col_1 = h_sin
col_2 = w - h_sin
rectangle_image = rotated[min(row_1, row_2): max(row_1, row_2), min(col_1, col_2): max(col_1, col_2)]

#cv2.imshow("Rectangle_image", rectangle_image)
#cv2.waitKey(0)

print("Введите коэффициент изменения длины")
k = float(input())
print("Введите признак используемой интерполяционной схемы ( 0 – нулевого порядка, 1 – первого порядка, 2- третьего порядка).")
i = int(input())
if k > 0 and k <=1:
    s = 1/k
    dim = (int(w*k), int(h*s))

    if i == 0:
        result = cv2.resize(rectangle_image, dim, interpolation = cv2.INTER_NEAREST)
    elif i == 1:
        result = cv2.resize(rectangle_image, dim, interpolation = cv2.INTER_LINEAR)
    elif i == 2:
        result = cv2.resize(rectangle_image, dim, interpolation = cv2.INTER_AREA)
    else:
        print("Неправильно введен признак используемой интерполяционной схемы")
    cv2.imshow("Result image", result)
    cv2.waitKey(0)

# запишем результирующее изображение на диск
    cv2.imwrite("result.jpg", result)
else:
    print("Коэффициент должен быть больше 0 и меньше или равен 1.")

cv2.destroyAllWindows()
