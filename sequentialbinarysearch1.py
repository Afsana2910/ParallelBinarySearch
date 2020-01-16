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

def duplicate(array,key):
    locations = []
    index = binarysearch(array,0,len(array)-1,key)
    locations.append(index)
    if index!=-1:
        loc = index
        while array[loc+1]==key:
            loc = loc + 1
            locations.append(loc)
        loc = index
        while array[loc-1]==key:
            loc = loc -1
            locations.append(loc)
            
        print(locations)
            
    else:
        print("Data not found")
            
            
        
t1 = time.clock()
data = np.arange(1000000000)
data = data.tolist()
duplicate(data,6)
print("Execution Time is :",time.clock()-t1)
