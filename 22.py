a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=b[:]

for i in range(a[0]):            
        c[i]=(c[i]+a[2])
        c[i]=c[i]%(2*a[1])
        while c[i]>a[1] or c[i]<0:
            c[i]=2*a[1]-c[i]



print(c)
