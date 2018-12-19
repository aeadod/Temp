n=int(input())
m=int(input())


yuanlai=[i+1 for i in range(n)]

for i in range(m):
    stu,pos=map(int,input().split())
    after=yuanlai.index(stu)+pos
    yuanlai.remove(stu)
    yuanlai.insert(after,stu)
print(' '.join(map(str,yuanlai)))
