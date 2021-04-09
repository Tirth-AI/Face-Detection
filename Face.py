# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:49:21 2021

@author: Tirth Dalwadi
"""


import cv2
cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:

    ret, frame = cap.read()
    if ret:
        faces = classifier.detectMultiScale(frame)
        for face in faces:
            x,y,w,h = face
            color = (0,0,255)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),color,6)
        cv2.imshow("Face",frame)
        

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

