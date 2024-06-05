# захват видео с веб-камеры

import cv2 as cv
import numpy as np

cam_port = 0
cap = cv.VideoCapture(cam_port)

# считываем ввод с камеры через цикл по кадрам
while True:
    ret, frame = cap.read()
    cv.imshow('video feed', frame)

    # прерывание цикла клавишей "Q"
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# "освобождаем" камеру
cap.release()
cv.destroyAllWindows()
