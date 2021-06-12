#!/usr/bin/env python
# coding: utf-8

# <h1 style="text-align:center">Face Detection</h1>

# In[1]:


import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img = cv2.imread('felix.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 2.0, 7)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

a=cv2.resize(img,(500,600))
cv2.imshow('img', a)
cv2.imwrite('result.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

