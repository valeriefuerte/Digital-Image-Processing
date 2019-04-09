import cv2
import numpy as np

img = cv2.imread('1.jpg',0)
img = cv2.medianBlur(img,5)
result = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(result,(i[0],i[1]),i[2],(255,0,0),2)
    cv2.circle(result,(i[0],i[1]),2,(255,0,0),3)

cv2.imshow('Circles',result)
cv2.imwrite("result.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
