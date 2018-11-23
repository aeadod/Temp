a=int(input())
alist=list(map(int,input().split()))
blist=[0]*1000
for i in range(a):
    blist[alist[i]]+=1
print(blist.index(max(blist)))
