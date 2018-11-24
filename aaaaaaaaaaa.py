def getnumber():
    nums=[]
    inumber=input(":")
    while inumber !='':
        nums.append(eval(inumber))
        inumber=input(":")
    return nums
def minn(nums):
    s=0.0
    for i in nums:
       s+=i
    return s/len(nums)
def fangcha(nums,minn):
    sdev=0.0
    for num in nums :
        sdev +=(num-minn)**2
    return pow(sdev/(len(nums)-1),0.5)
def median(nums):
    sorted(nums)
    size=len(nums)
    if size %2==0:
        return ((nums[size//2-1]+nums[size//2])/2)
        
    else :
        return nums[size//2]
n=getnumber()
m=minn(n)
print('{},{:.2f},{}'.format(m,fangcha(n,m),median(n)))
