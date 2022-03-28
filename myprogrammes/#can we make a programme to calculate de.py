#can we make a programme to calculate determinant
def determinant(x_1,x_2,x_3,y_1,y_2,y_3,z_1,z_2,z_3):
    return x_1*(y_2*z_3 - z_2*y_3) - x_2*(y_1*z_3 - z_1*y_3) + x_3*(y_1*z_2 - z_1*y_2)


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

print(determinant(list1[0][0],list1[0][1],list1[0][2],list1[1][0],list1[1][1],list1[1][2],list1[2][0],list1[2][1],list1[2][2]))