import mydeterminant

xco=[]
yco=[]
zco=[]
for i in range(3):
    b=int(input("enter the first row elements"))
    xco.append(b)

for i in range(3):
    c=int(input("enter the second row elements"))
    yco.append(c)

for i in range(3):
    d=int(input("enter the third row elements"))
    zco.append(d)


list1 = [xco,yco,zco]

print(mydeterminant.determinant(list1[0][0],list1[0][1],list1[0][2],list1[1][0],list1[1][1],list1[1][2],list1[2][0],list1[2][1],list1[2][2]))
