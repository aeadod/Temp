geshu=int(input())
alist=list(map(int ,input().split()))
alist.sort()
smallthan=0
bigthan=0
for i in alist:
    if i<alist[int(geshu/2)]:
        smallthan+=1
    elif i>alist[int(geshu/2)]:
        bigthan+=1
if bigthan==smallthan:
    print(alist[int(geshu/2)])
else :
    print(-1)
