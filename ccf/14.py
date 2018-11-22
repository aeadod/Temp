x=int(input())
alist=list(map(int ,input().split()))
  
cha=(alist[1]-alist[0]) if alist[1]>alist[0] else (alist[0]-alist[1])
for i in range(2,x):
    for j in range(1,x):
        if((alist[i]-alist[i-j]) if alist[i]>alist[i-j] else (alist[i-j]-alist[i]))<cha:
            cha=((alist[i]-alist[i-j]) if alist[i]>alist[i-j] else (alist[i-j]-alist[i]))   
        
print(cha)
