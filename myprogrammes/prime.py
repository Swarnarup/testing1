# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:14:41 2021

@author: Swarnarup
"""

n=int(input())
l=[]
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i not in l:
                l.append(i)
print(l)