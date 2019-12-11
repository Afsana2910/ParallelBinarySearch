# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:21:54 2019

@author: Afsana
"""
import numpy as np
import math
import time
def binarysearch(a,low,high,e):
    while low <= high:
        center = int(math.floor(low + (high-low)/2))
        if a[center] == e:
            return center
        elif a[center] > e:
            high = center - 1
        else:
            low = center + 1
    
    return -1

t1 = time.clock()
data = np.arange(1000000000)
data = data.tolist()
print(binarysearch(data,0,len(data)-1,3))
print("Execution Time is :",time.clock()-t1)