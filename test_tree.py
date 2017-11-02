import numpy as np
import itertools as it
import random as rd
import time as time
import cProfile


INF=float('inf')

def calc_time(tasks, born):
    m1=   tasks[0][0]
    m2=m1+tasks[0][1]
    m3=m2+tasks[0][2]
    #le calcule du temps se fait en temps linaire
    for i in range(1,len(tasks)):
        if born < m1:
            m3=INF
            return m3
        m1=m1+tasks[i][0]
        if born < m2:
            m3=INF
            return m3
        if m1<m2:
            m2=m2+tasks[i][1] #m2+ curr task de m2
        else:
            m2=m1+tasks[i][1] #m1+ curr task de m2
        if born < m3:
            m3=INF
            return m3
        if m2<m3:
            m3=m3+tasks[i][2]
        else:
            m3=m2+tasks[i][2]
    #print (m3)
    return m3

def tree(taskin):
    #taskin.sort()
    bestperm=[]
    borninf=calc_time(taskin,float('inf'))
    bestperm = taskin[:]
    for permutation in it.permutations(taskin):
        res = calc_time(permutation,borninf)
        if borninf > res:
            borninf = res
            bestperm=permutation
            #print(borninf, bestperm)
    print('temp =',borninf,'best perm=',bestperm)

num=[[rd.randrange(1,100) for __ in range(3)] for _ in range(3)]
print(num)

tasks=[[9,4,1],
        [2,3,4],
        [3,3,5],
        [4,5,4],
        [8,1,1]]
        
start = time.time()
tree(num)
end = time.time()
print(end-start)


#num=[[rd.randint(1,100)]*3 for _ in range(10)]

#pgv = [[0] * (cmax + 1) for _ in range(n)]