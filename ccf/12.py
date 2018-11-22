
x=int(input())
h=[]
w=[]
lst=[0]*1000000
for i in range(x):
    h.append(tuple(map(int,input().split())))

for i in range(x):
    w.append(tuple(map(int,input().split())))
times=0
for i in range(x):
    for j in range(h[i][0],h[i][1]):
            lst[j]+=1
for i in range(x):
    for j in range(w[i][0],w[i][1]):
            lst[j]+=1
for i in range(1000000):
    if(lst[i]>1):
        times+=1
print(times)
