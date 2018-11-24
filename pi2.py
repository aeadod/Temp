from random import random
from time import perf_counter
data=1000*100000
hits=0
start = perf_counter()
for i in range(1,data+1):
    x,y = random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist <=1.0:
        hits+=1
pi=4*(hits/data)
print("{}".format(pi))
print("{:.5f}s".format(perf_counter()-start))
