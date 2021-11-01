#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[1]:


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# # Define Blur Function From Scratch

# In[2]:


def mean_blur(mean_img, ksize):
    mean_img = np.array(mean_img)
    offset = ksize - 1 #index start from 0
    for i in range(mean_img.shape[0] - offset): 
        for j in range(mean_img.shape[1] - offset):
            arr = np.array(mean_img[i:(i + ksize), j:(j + ksize)]).flatten()
            mean = np.mean(arr)
            mean_img[i + ksize // 2, j+ksize // 2] = mean #/ = return double, // = return int 
    return mean_img

def mean_blur_padding(mean_pad_img, ksize):
    mean_pad_img = np.array(mean_pad_img)
    offset = ksize - 1 #start index 1 -> 0
    mean_pad = np.pad(mean_pad_img, ksize // 2)
    for i in range(mean_pad.shape[0] - offset): 
        for j in range(mean_pad.shape[1] - offset):
            arr = np.array(mean_pad[i:(i + ksize), j:(j + ksize)]).flatten()
            mean = np.mean(arr)
            mean_pad[i + ksize // 2, j + ksize // 2] = mean
    mean_img_pad = mean_pad[ksize // 2:mean_pad.shape[0] - ksize // 2, ksize // 2:mean_pad.shape[1] - ksize // 2]
    return mean_pad

def median_blur(med_img,ksize):
    med_img = np.array(med_img)
    offset = ksize - 1
    for i in range(med_img.shape[0] - offset): 
        for j in range(med_img.shape[1] - offset):
            arr = np.array(med_img[i:(i + ksize), j:(j + ksize)]).flatten()
            median = np.median(arr)
            med_img[i + ksize // 2, j + ksize // 2] = median
    return med_img

def median_blur_padding(med_pad_img,ksize):
    med_pad_img = np.array(med_pad_img)
    offset = ksize - 1
    med_pad = np.pad(med_pad_img,ksize // 2)
    for i in range(med_pad.shape[0] - offset): 
        for j in range(med_pad.shape[1] - offset):
            arr = np.array(med_pad[i:(i + ksize), j:(j + ksize)]).flatten()
            median = np.median(arr)
            med_pad[i + ksize // 2, j + ksize // 2] = median
    median_img_pad = med_pad[ksize // 2:med_pad.shape[0] - ksize // 2, ksize // 2:med_pad.shape[1] - ksize // 2]
    return med_pad

img = Image.open('Assets/sample.jpg').convert('L')
mean_pad_out = mean_blur_padding(img,7)
mean_out = mean_blur(img,7)
median_pad_out = median_blur_padding(img,7)
median_out = median_blur(img,7)

out = [mean_pad_out, mean_out, median_pad_out, median_out]
title = ["Mean Padding", "Mean No Padding", "Median Padding", "Median No Padding"]

plt.figure(figsize=(16, 16))
for i in range(len(out)):
    plt.subplot(3, 3, i + 1)
    plt.title(title[i])
    plt.imshow(out[i], 'gray')
    plt.xticks([]),plt.yticks([])

