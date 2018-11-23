a=int(input())
alist=list(map(int,input().split()))
blist=[1]*a
for i in range(a):
    for j in range(i+1,a):
        if (alist[j]==alist[i]) :
            blist[j]+=1

for i in range(a):
    print(blist[i],end=' ')
