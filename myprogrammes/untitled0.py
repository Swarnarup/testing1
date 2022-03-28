# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:31:39 2022

@author: Swarnarup
"""
i = [1,2,'(',')']
def checkParan(inpExpn):
    # Write your code here
    
    x=[]
    y=[]
    for i in range(len(inpExpn)):
        x.append(inpExpn[i])
        y.append(i)
    
    def check(l1,l2):
        if len(l1)==0:
            return 'match'
        if (l1[0]=='(' and l1[-1]=='') or (l1[0]=='[' and l1[-1]==']'):
            l1.pop(0)
            l1.pop(-1)
            l2.pop(0)
            l2.pop(-1)
        if l1[0] in [')',']']:
            return l2[0]
        else:
            return l2[-1]
        check(l1,l2)
        
    check(x,y)
    
checkParan(i)