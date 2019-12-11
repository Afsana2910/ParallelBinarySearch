# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:12:11 2019

@author: Afsana
"""

import math
from mpi4py import MPI
import numpy as np
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

def addtolist(l,a):
    if a>=0:
        l.append(a)
    
        


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
t1=time()

#your program

comm.Barrier()

if rank ==0:
    data = np.arange(1000)
    chunksize = (data.shape[0])/4
    index = []
    answers = []
    key = 3
    Mandkey = [chunksize,key]
    data_split = np.split(data,4)
    comm.send(Mandkey, dest=1, tag=300)
    comm.send(Mandkey, dest=2, tag=301)
    comm.send(Mandkey, dest=3, tag=302)
    comm.send(Mandkey, dest=4, tag=303)
    
    slice1 = np.asarray(data_split[0])
    slice2 = np.asarray(data_split[1])
    slice3 = np.asarray(data_split[2])
    slice4 = np.asarray(data_split[3])
    comm.send(slice1, dest=1, tag=100)
    comm.send(slice2, dest=2, tag=101)
    comm.send(slice3, dest=3, tag=102)
    comm.send(slice4, dest=4, tag=103)
        
    res1 = comm.recv(source=1, tag=200)
    res2 = comm.recv(source=2, tag=201)
    res3 = comm.recv(source=3, tag=202)
    res4 = comm.recv(source=4, tag=203)
    answers.append(res1)
    answers.append(res2)
    answers.append(res3)
    answers.append(res4)
    for i in range(len(answers)-1):
        addtolist(index,answers[i])
    if(len(index)!=0):
            print("Found at index ", index)
    else:
        print("Is not present")
    print('Execution time: ',  time()-t1)
   
        
        
if rank==1:
    
    array = comm.recv(source=0, tag=100)
    mk = comm.recv(source=0, tag=300)
    key = mk[1]
    left = array[0]
    right = array[array.shape[0]-1]
    if(key<left or key>right):
            
        res=-1
    elif(key==left):
        res = 0
    elif(key == right):
        res = array.shape[0]-1
        
    else:
        res = binarysearch(array,0,(array.shape[0]-1),key)
           
    comm.send(res, dest=0, tag=200)
    print('Execution time: ',  time()-t1)
            
elif rank==2:
    array = comm.recv(source=0, tag=101)
    mk = comm.recv(source=0, tag=301)
    M = mk[0]
    key = mk[1]
    left = array[0]
    right = array[array.shape[0]-1]
    if(key<left or key>right):
            
        res = -1
    elif(key==left):
        res = 0
        res = res+M
    elif(key == right):
        res = array.shape[0]-1
        res = res+M
    else:
        res = binarysearch(array,0,array.shape[0]-1,key)
        res = res+M
            
    comm.send(res, dest=0, tag=201)
    print('Execution time: ',  time()-t1)
elif rank==3:
    array = comm.recv(source=0, tag=102)
    mk = comm.recv(source=0, tag=302)
    M = mk[0]
    key = mk[1]
    left = array[0]
    right = array[array.shape[0]-1]
    if(key<left or key>right):
           
        res = -1
    elif(key==left):
        res = 0
        res = res + (2*M)
    elif(key == right):
        res = array.shape[0]-1
        res = res + (2*M)
    else:
        res = binarysearch(array,0,array.shape[0]-1,key)
        res = res + (2*M)
            
    comm.send(res, dest=0, tag=202)
    print('Execution time: ',  time()-t1)
elif rank==4:
    array = comm.recv(source=0, tag=103)
    mk = comm.recv(source=0, tag=303)
    M = mk[0]
    key = mk[1]
    left = array[0]
    right = array[array.shape[0]-1]
    if(key<left or key>right):
            
        res = 1
    elif(key==left):
        res = 0
        res = res + (3*M)
    elif(key == right):
        res = array.shape[0]-1
        res = res + (3*M)
    else:
        res = binarysearch(array,0,array.shape[0]-1,key)
        res = res + (3*M)
           
    comm.send(res, dest=0, tag=203)
    print('Execution time: ',  time()-t1)
            





