#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:36:19 2018

@author: yeqiming
"""

import pandas as pd
import numpy as np

def Locate(m,row):
    x = []
    for i in range(row):
        tot = np.sum(m[i,:])
        if tot == 0:
            x.append(0)
        else:
            k = np.argwhere(m[i,:]==1)[0,0]+1
            x.append(k)
    for j in range(1,len(x)):
        if x[j] == 0:
            x[j] = x[j-1]
    return x

def GetPositions(f1,f2,f3):
    li = pd.read_csv(f1,header=None)
    l = pd.read_csv(f2,header=None)
    m = pd.read_csv(f3,header=None)
    m1 = np.array(l)
    m2 = np.array(m)
    l3 = np.array(li)
    row1 = np.shape(m1)[0]
    row2 = np.shape(m2)[0]
    
    lis1 = Locate(m1,row1)
    lis2 = Locate(m2,row2)

    NP = np.array([lis1,lis2])
    
    return(l3, NP)