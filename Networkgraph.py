#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:43:31 2018

@author: yeqiming
"""

import numpy as np
from Read import GetPositions
from Plot import PlotPath


# read file #
f1 = 'coordinates.csv'
f2 = 'truckSol_test.csv'
f3 = 'droneSol_test.csv'
lis, move = GetPositions(f1,f2,f3)
num_nodes = np.shape(lis)[0]
PlotPath(lis,move,num_nodes)









