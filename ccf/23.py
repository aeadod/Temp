x,y=list(map(int,input().split()))
img=[]
for i in range(x):
    a=list(map(int,input().split()))
    img.append(a)

for i in range(y):
    for j in range(x):
        print(img[j][y-i-1],end=' ')
    print()
