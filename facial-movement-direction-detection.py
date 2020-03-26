#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:10:13 2020

@author: ashrafi
"""

import cv2
import numpy as np
import dlib
import os

temp=0


def rignt():
    print('rignt')
    temp +1


def lent():
    print('lent')
    temp +2

cal = lambda x0, x1 : x1-x0

pradect= dlib.shape_predictor(os.path.join(os.getcwd(),'68_face_landmarks.dat') )
detect= dlib.get_frontal_face_detector()

cap= cv2.VideoCapture(0)

#img=cv2.imread('/home/ashrafi/Pictures/right.png')

while cap.isOpened():
    ref, img= cap.read()
    faces = detect(img)
    for face in faces:
        landmarks = pradect(img, face)

        x0 = landmarks.part(0).x
        x36 = landmarks.part(36).x
        x45 = landmarks.part(45).x
        x16 = landmarks.part(16).x

        left = cal(x36, x0)
        right = cal(x16, x45)
        value = right-left

        if value > 10:
            cv2.putText(img, 'Left', (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,255,0), 2)
            temp =2
        elif value < -10:
            cv2.putText(img, 'right', (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,255,0), 2)
            temp =1
        else:
            cv2.putText(img, 'font', (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
            temp=0
    '''
    if temp == 3:
        continue

    elif temp == 2:
        left()

    elif temp == 1:
        right()
    '''


    cv2.imshow('frame', img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
