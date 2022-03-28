"""
BINARY SEARCH
"""

def bsearch(inplist , num):
    inplist.sort()
    l=len(inplist)
    if inplist[l//2]==num:
        return l//2
    if inplist[l//2]>num:
        return bsearch(inplist[:(l//2)] , num)
    if inplist[l//2]<num:
        return bsearch(inplist[(l//2):] , num)



a=[1,5,2,8,4,0,3,14,65,34,23,6]
b=4
bsearch(a,b)

