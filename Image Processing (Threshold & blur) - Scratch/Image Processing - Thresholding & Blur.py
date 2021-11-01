#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# # Thresholding with OpenCV

# In[2]:


img = cv2.imread('iu.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bin_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_BINARY)
_, inv_bin_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_BINARY_INV)
_, trunc_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_TRUNC)
_, to_zero_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_TOZERO)
_, inv_to_zero_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_TOZERO_INV)
_, otsu_thres = cv2.threshold(gray_img, 127,255, cv2.THRESH_OTSU)
adap_mean_thres = cv2.adaptiveThreshold(gray_img, 127, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
adap_gaus_thres = cv2.adaptiveThreshold(gray_img, 127, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)

result = [bin_thres,inv_bin_thres,trunc_thres,to_zero_thres,inv_to_zero_thres,otsu_thres,adap_mean_thres,adap_gaus_thres]
result_title = ['BINARY','INV BINARY','TRUNC','TO ZERO','INV TO ZERO','OTSU','ADAP MEAN','ADAP GAUS']
plt.figure(figsize=(16,16))
for i,(curr_img,curr_title) in enumerate(zip(result,result_title)):
    plt.subplot(3,3,(i+1))
    plt.imshow(curr_img,'gray')
    plt.title(curr_title)
    plt.xticks([]),plt.yticks([])


# # Using OpenCV

# In[3]:


img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur_img = cv2.blur(img,(16,16)) #mean blur
median_blur = cv2.medianBlur(img, 11) #best for small noise like salt & pepper, also vanishing acne
gauss_blur = cv2.GaussianBlur(img, (11,11),5.0) #similar to mean but smoother
bilateral_blur = cv2.bilateralFilter(img,11,150,150) #remove small noise to sharpen the image
result = [blur_img,median_blur,gauss_blur,bilateral_blur]
result_title = ['BLUR','MEDIAN BLUR','GAUS BLUR','BILATERAL BLUR']
plt.figure(figsize=(15,15))
for i,(curr_img,curr_title) in enumerate(zip(result,result_title)):
    plt.subplot(3,3,(i+1))
    plt.imshow(curr_img,'gray')
    plt.title(curr_title)
    plt.xticks([]),plt.yticks([])

