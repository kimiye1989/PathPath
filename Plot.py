#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:58:43 2018

@author: yeqiming
"""

import matplotlib.pyplot as plt
import numpy as np
import os

def PlotPath(lists,mv,num):
    os.chdir('/Users/yeqiming/Desktop/NetworkGraph 2/Output')
    
    plt.scatter([],[],color = 'red', label = 'Truck')
    plt.scatter([],[],color = 'green', label = 'Drone')
    plt.plot([],[],color = 'red', label = "Truck's Last Path")
    plt.plot([],[],color = 'green', label = "Drone's Last Path")
    
    list_x = []
    list_y = []
    
    for i in range(num):
        plt.scatter(lists[i][1], lists[i][2], s=30,color='grey')
        list_x.append(lists[i][1])
        list_y.append(lists[i][2])
    
    plt.xlim(min(list_x)-2, max(list_x)+2)
    plt.ylim(min(list_y)-2, max(list_y)+2)
        
    plt.xticks(np.arange(min(list_x)-2, max(list_x)+2, 1.0))
    plt.yticks(np.arange(min(list_y)-2, max(list_y)+2, 1.0))
    
    num_agents = np.shape(mv)[0]
    num_ticks = np.shape(mv)[1]
        
    #plot initial point:
        
    for i in range(num_agents):
        init_nod = mv[i,0]
            
        state_x =lists[init_nod-1,1]
        state_y =lists[init_nod-1,2]
            
        if i%2 != 0:
            present_color = 'red'
            post_color = 'lightgrey'
        else:
            present_color = 'green'
            post_color = 'darkgrey'
            
        plt.scatter(state_x, state_y, color = present_color, s = 30)
        
    plt.title('Step_1')
    plt.savefig('Step_1.png')
        
        
    for j in range(1,num_ticks+1):
                    
        #plot all nodes
        for k in range(num):
            plt.scatter(lists[k-1][1], lists[k-1][2], s=30,color='grey')
        
        for i in range(num_agents):
            seq = mv[i][0:j]
            
            #print('the seq is: ', seq)
                
            if i%2 != 0:
                present_color = 'red'
                post_color = 'lightgrey'
            else:
                present_color = 'green'
                post_color = 'darkgrey'
    
                 
            #plot current nodes
            currnode = seq[-1]
            plt.scatter(lists[currnode-1][1],lists[currnode-1][2], color = present_color, s = 30)
    
                
            #plot routes
            if len(seq) >= 2:
                
                listx = []
                listy = []
    
                for xy in seq:
                        
                    listx.append(lists[xy-1][1])
                    listy.append(lists[xy-1][2])
                    
                #print('listx is: ', listx)
                #print('listy is: ', listy)
                #print('x_till_last is:',listx[:-1])
                #print('y_till_last is:',listy[:-1])
                #print('x pre-last is:',[listx[-2],listx[-1]])
                #print('y pre-last is:',[listy[-2],listy[-1]])
                        
                plt.plot([listx[-2],listx[-1]],[listy[-2],listy[-1]],color=present_color, linewidth=1)
                plt.plot(listx[:-1],listy[:-1],color=post_color, linewidth=1)
    
        
            
        plt.legend(loc = 'upper right')
        plt.grid(which='major', axis='both')
        plt.title('Step_%d'%(j))
        plt.savefig('Step_%d.png'%(j))
        #print('______________________________')