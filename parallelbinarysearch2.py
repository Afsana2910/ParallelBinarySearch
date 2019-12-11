# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:56:03 2019

@author: Afsana
"""

import math
import numpy as np
from mpi4py import MPI
from time import time
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

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
data = np.arange(20)
data = data.tolist()
keys = [3,100,99,30]
t0=time()


comm.Barrier()
if rank ==0:
    
    comm.send(data, dest=1, tag=100)
    comm.send(data, dest=2, tag=101)
    comm.send(data, dest=3, tag=102)
    comm.send(data, dest=4, tag=103)
    comm.send(keys[0], dest=1, tag=200)
    comm.send(keys[1], dest=2, tag=201)
    comm.send(keys[2], dest=3, tag=202)
    comm.send(keys[3], dest=4, tag=203)
    
if rank ==1:
    
    array = comm.recv(source=0, tag=100)
    k = comm.recv(source=0, tag=200)
    res = binarysearch(array,0,len(array)-1,k)
    if res!=-1:
        print(k," is at index ",res)
    else:
        print(k," is not present")

    print("Time in process 1 is ",time()-t0)
elif rank==2:
  
    array = comm.recv(source=0, tag=101)
    k = comm.recv(source=0, tag=201)
    res = binarysearch(array,0,len(array)-1,k)
    if res!=-1:
        print(k," is at index ",res)
    else:
        print(k," is not present")
    
    print("Time in process 2 is ",time()-t0)
elif rank==3:
   
    array = comm.recv(source=0, tag=102)
    k = comm.recv(source=0, tag=202)
    res = binarysearch(array,0,len(array)-1,k)
    if res!=-1:
        print(k," is at index ",res)
    else:
        print(k," is not present")
    
    print("Time in process 3 is ",time()-t0)
elif rank==4:
    
    array = comm.recv(source=0, tag=103)
    k = comm.recv(source=0, tag=203)
    res = binarysearch(array,0,len(array)-1,k)
    if res!=-1:
        print(k," is at index ",res)
    else:
        print(k," is not present")
   
    print("Time in process 4 is ",time()-t0)

    