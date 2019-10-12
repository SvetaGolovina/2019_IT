#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[12]:


def get_indices(N, n_batches, split_ratio):
    k=((N-1)*(1+split_ratio))/((n_batches-1)*split_ratio+1+split_ratio)
    return k


# In[16]:


inds = np.array([0, 0, 0])
N = 100
n_batches = 5
split_ratio = 0.25
k = get_indices(N,n_batches, split_ratio)
inds[1]=k/(1+split_ratio)
inds[2]=k
it = inds[2] - inds[1]
print(inds)
for i in range (1,n_batches):
    inds += it
    print(inds)


# In[ ]:




