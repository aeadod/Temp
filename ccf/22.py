x=int(input())
alist=list(map(int,input().split()))

flag=1
for i in range(x-1):
    if alist[i+1]!=alist[i]:
        flag+=1
print(flag)
