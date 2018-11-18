import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier(r'C:\Users\jojoj\Desktop\Machine_Learning\Workspace\opencv-3.4\opencv-3.4\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(r'C:\Users\jojoj\Desktop\Machine_Learning\Workspace\opencv-3.4\opencv-3.4\data\haarcascades\haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # on img, starting point, ending point, color=blue, line_width=2
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        # Region of the face (just goes y then x)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    cv.imshow('img', img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()