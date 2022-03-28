# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:41:16 2021

@author: Swarnarup
"""

minuite=int(input('enter minuite'))
if minuite<59:
    p=minuite*100/60
    print('percentage of hour is '+str(p))
elif minuite==60:
    print('an hour')
else:
    print('cant exceed 60 min.7060')