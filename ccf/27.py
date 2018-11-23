n = int(input())
a = list(map(int,input().split()))
flag=0
a.sort()
for i in range(1,n):
    if a[i]-a[i-1]==1 or a[i-1]-a[i]==1:
        flag+=1
print(flag)
