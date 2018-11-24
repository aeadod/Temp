count=0
def hannuota (n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count+=1
    else :
        
        hannuota(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        hannuota(n-1,mid,dst,src)
hannuota(3,'A','C','B')
print(count)
