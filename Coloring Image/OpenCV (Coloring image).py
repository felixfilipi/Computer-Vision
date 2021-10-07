#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

img = cv2.imread("Source.jpeg")
img[:350,500:,2]=0 #[Top_right_start:btm_size,left_start:until end, color] = parameter color
img[350:,500:,0]=0 
img[350:,:500:,1]=0 
img[:350,:500:,0]=50

cv2.imshow("Title",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imwrite("Result.jpg",img)

