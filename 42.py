n,k = map(int,input().split())
taket = {}
returnt = {}
timeline = {}
for i in range(k):
    w,s,c = map(int,input().split())
    if(s not in timeline):#借钥匙
        timeline[s]=[]
    timeline[s] += [w]
    timeline[s].sort()
    if(s+c not in timeline):#还钥匙
        timeline[s+c]=[]
    timeline[s+c] += [-(n-w)]#方便排序,从小到大归还
    timeline[s+c].sort()
 
box = list(range(1,n+1))
 
for t in sorted(timeline.keys()):
    for x in timeline[t]:
        if(x <= 0):#还钥匙
            box[box.index(0)] = n+x
        else:#借钥匙
            box[box.index(x)] = 0
print(" ".join(map(str,box)))
