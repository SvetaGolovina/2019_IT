#!/usr/bin/env python
# coding: utf-8

# In[125]:


import matplotlib.pyplot as plt
import numpy as np


# In[126]:


import math
from math import pi, sqrt, exp


# In[127]:


def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return


def get_kernel(ws):
    sig =1
    p = ws//2
    kernel = np.zeros((5,5))
    for i in range(ws): # foreach row
        for j in range(ws): # foreach column
            kernel[i,j] =  exp(-abs((i-p)**2+(j-p)**2)/(2*sig*sig))/(2*pi*sig*sig)

    return kernel

def filter(img, window_size=5):
    img2 = np.zeros_like(img)
    kernel = get_kernel(window_size)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


# In[128]:


img = plt.imread("C:/Git/2019_IT/img.png")[:,:,:3]
# add_noise(img)
img2 = filter(img)

fig, axs = plt.subplots(1,2)
axs[0].imshow(img)
axs[1].imshow(img2)
plt.show()


# In[ ]:




