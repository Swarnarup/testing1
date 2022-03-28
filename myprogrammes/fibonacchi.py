# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:52:38 2021

@author: Swarnarup
"""

'fibonacchi'
import time

"""
length=int(input())
a=int(input('enter first element'))
b=int(input('enter second element')) 
"""
def fibonacchi_list(a,b,length):
    l=[]
    x=a
    y=b
    l.append(a)
    l.append(b)
    for i in range(length):
        z=x+y
        l.append(z)
        x,y=y,z
    return l


t_1=time.perf_counter()
fibonacchi_list(100,100,100)
t_2=time.perf_counter()
print(t_2-t_1)