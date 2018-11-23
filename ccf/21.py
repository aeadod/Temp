a=int(input())
b=0
c=len(str(a))
for i in range (c):
    b=b+a%10
    a=a//10
print(b)
