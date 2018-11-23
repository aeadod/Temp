n = int(input())
a = list(map(int,input().split()))
flag=0
for i in range(n):
    for j in range(i+1,n):
        if a[j]==-a[i]:
            flag+=1
print(flag)
