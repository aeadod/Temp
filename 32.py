n,k=map(int,input().split())
a=[1]*n
b=[i+1 for i in range(n)]
while a.count(1)!=1:
    for i in range(n):
        if b[i]%k==0 or b[i]%10==k:
            a[i]=0







print(a.find(1)+1)
