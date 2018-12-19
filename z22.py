n,L,t=map(int,input().split())
pos = list(map(int,input().split()))
dire=[1]*n
for ti in range(t):
    for i in range(n):
        if(pos[i]==L):
            dire[i]=-1
        if(pos[i]==0):
            dire[i]=1
        pos [i]+=dire[i]
    for i in range(n):
        for j in range(i+1,n):
            if (pos[i]==pos[j]):
                dire[i]=-dire[i]
                dire[j]=-dire[j]
print(' '.join(str(i) for i in pos))
