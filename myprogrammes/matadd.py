
"""
Created on Fri Dec 17 09:21:57 2021

@author: Swarnarup
"""

mtrix1 = list(input())
mtrix2 = list(input())
def addmat(matrix1,matrix2):
    list1 = []
    for i in range(3):
        list2 = []
        for j in range(3):
            m = matrix1[i][j] + matrix2[i][j]
            list2.append(m)
        list1.append(list2)
    return list1
print(addmat(mtrix1,mtrix2))