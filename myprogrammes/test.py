def s(n):
    if n==0:
        return 0
    else:
        return (n+s(n-1))

import time
t=time.perf_counter()
print(s(100))
t2=time.perf_counter()


s=0
a=time.perf_counter()
for i in range(101):
    s+=i
print(s)
b=time.perf_counter()
print(t2-t)
print(b-a)
print(b-a-t2+t)
