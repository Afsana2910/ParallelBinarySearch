# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:21:54 2019

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
keys = [3,100,99,30]
data = np.arange(100000000)
data = data.tolist()
t1 = time.clock()
for i in range(len(keys)-1):
    print(binarysearch(data,0,len(data)-1,keys[i]))
print("Execution Time is :",time.clock()-t1)