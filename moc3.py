import time
scale=10
print('{0:-^20}'.format("start"))

for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))

print("{0:-^20}".format("end"))
