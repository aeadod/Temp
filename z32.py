n,k = map(int,input().split())
l=[i+1 for i in range(n)]
num=1
while len(l)>0:
    keys_del=[]
    for key,value in enumerate(l):
        if(num%k ==0 or num%10 == k):
            keys_del.append(key)
        num+=1
    account=0
    for key in keys_del:
        del l[key-account]
        account+=1
        if len(l)==1:
            print(l[0])
