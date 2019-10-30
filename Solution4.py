#!/usr/bin/env python
# coding: utf-8

import numpy as np
import random as r
import matplotlib.pyplot as plt
from math import pi, sin, cos


def is_pareto(x):
    x0 = np.ones(x.shape[0], dtype = bool)
    for i, c in enumerate(x):
        x0[i] = np.all(np.any(x[:i]>c, axis=1)) and np.all(np.any(x[i+1:]>c, axis=1))
    return x0


def rotation_matrix(x):
    return np.array([[cos(x), sin(x)],[-sin(x), cos(x)]])


def coord_sys(x,m,pf):
    y=np.array([max_el,0])
    for i in range(m):
        y1 = np.dot(rotation_matrix(2*pi*i/m),y)
        #print(y1)

        plt.plot([0,y1[0]], 
                 [0,y1[1]],
                 linewidth = 1,
                 color = 'black')

        plt.annotate( f"y{i+1}",(y1[0],y1[1]))
   
    x1 = np.zeros((n,m,2)) 
    x1[:,:,0] = np.copy(x)
    #print(x1)
    
    y2 = np.zeros((n,m,2)) 
    for j in range(n):
        for i in range(m):
            y2[j,i,:] = np.dot(rotation_matrix(2*pi*i/m),x1[j,i,:])

    for j in range(n):
        plt.scatter(y2[j,:,0], y2[j,:,1], alpha=0.6)
        if (pf[i]):
            plt.plot(y2[j,:,0], y2[j,:,1], alpha=0.6)




n = 6
m = 5
max_el=10

x = np.array([[r.randint(0,max_el) for i in range(m)] for j in range(n)])
#print(x)

#булевские отметки парето фронт
pf = is_pareto(x)
#print(ixs)

#график
coord_sys(x,m,pf)

