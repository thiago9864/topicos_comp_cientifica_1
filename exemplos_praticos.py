# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:17:17 2019

@author: Thiago
"""

import matplotlib.pyplot as plt
import numpy as np

#Exercicios

# 1) 

#intervalo de tempo
t0 = 0.0 
tf = 100.0

#condição inicial
a0=0
b0=100
k1 = 0.1 #k+
k2 = 0.1 #k-

n = 100
dt = (tf - t0) / (n-1)
t = np.linspace(t0, tf, n)

#arrays de solução
a = np.zeros([n])
b = np.zeros([n])

#aplica condição inicial
a[0] = a0
b[0] = b0

#calcula metodo
for i in range(1,n):
    a[i] = dt * (-k1*a[i-1] + k2*b[i-1]) + a[i-1]
    b[i] = dt * (k1*a[i-1] - k2*b[i-1]) + b[i-1]
    
#Visualizando as soluções
plt.plot(t, a, 'r', label=u'A')
plt.plot(t, b, 'b', label=u'B')

plt.legend(loc='upper right')

plt.show()

