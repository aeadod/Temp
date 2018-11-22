n=int(input())

alist=list(map(int,input().split()))

for i in range(n):
    if i==0:
        print((alist[0]+alist[1])//2,end=' ')
    elif i==n-1:
        print((alist[-1]+alist[-2])//2,end=' ')
    else :
        print((alist[i]+alist[i-1]+alist[i+1])//3,end=' ')

