x=int(input())
alist=list(map(int,input().split()))
items=0
for i in range(1,x-1):
    if((alist[i-1]<alist[i]>alist[i+1])or(alist[i+1]>alist[i]<alist[i-1])):
        items+=1
print(items)
