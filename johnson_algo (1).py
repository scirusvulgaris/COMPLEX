#3600592 - Iurie TOMA
#Implementation d'algorithm Johnson pout 2 Machine
#Complexite O(n^2)

import pickle as pkl
import time
import matplotlib.pyplot as plt
import numpy as np
import random
import cProfile

#tache a traiter
listt = [[9,5],
        [2,1],
        [3,5],
        [5,5],
        [2,5]]
        
print('tache donnee',listt)
#initialisation des lists 
A=[]
B=[]
new_list=[]

#trouver la tache minimale
def find_min(tasks):
    supp=supp1=0
    minn_0=minn_1=float('inf')
    
    for i in range(len(tasks)):
        if len(tasks)==1:
            if tasks[0][0]<tasks[0][1]:
                minn_0=tasks[i][0]
                supp = i
                break
            else:
                minn_1=tasks[i][1]
                supp = i
                break
        
        minn_0=tasks[0][0]
        if minn_0>tasks[i][0]:
            minn_0=tasks[i][0]        
            supp= i
       
        minn_1=tasks[0][1]
        if minn_1>tasks[i][1]:
            minn_1=tasks[i][1] 
            supp1 = i

    if minn_0 < minn_1 and minn_0:
        A.append(tasks[supp])
        del tasks[supp]
    else:
        B.append(tasks[supp1])
        del tasks[supp1]
        #temp_list=A+B
        #print(calc_time(temp_list))
    return

def sort_l():
    while len(listt)!=0:
        find_min(listt)
        
#appel de lq function
sort_l()
B.reverse()
new_list=A+B

#calcule le temps d'execution
def calc_time(tasks):
    m1=tasks[0][0]
    m2=m1+tasks[0][1]
    for i in range(1,len(tasks)):
        m1=m1+tasks[i][0]
        if m1<m2:
            m2=m2+tasks[i][1] #m2+ curr task de m2
        else:
            m2=m1+tasks[i][1] #m1+ curr task de m2
    return m2
print('nouveau ordonnancement ',new_list)
print("meilleur temps d'execution:",calc_time(new_list))