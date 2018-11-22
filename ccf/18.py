x=int(input())
alist=list(map(int,input().split()))

if alist[1]>=alist[0]:
    cha=(alist[1]-alist[0]) 
else:
    cha=(alist[0]-alist[1])
for i in range(2,x):
    if(((alist[i]-alist[i-1]) if alist[i]>alist[i-1] else (alist[i-1]-alist[i]))>cha):
        cha=((alist[i]-alist[i-1]) if alist[i]>alist[i-1] else (alist[i-1]-alist[i]))
print(cha)
