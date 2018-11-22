n,k=list(map(int,input().split()))
alist=list(map(int,input().split()))
nowk=0
f=0
for i in alist:
    nowk+=i
    if(nowk>=k):
        nowk=0
        f+=1
if(nowk!=0):
    f+=1
print(f)
