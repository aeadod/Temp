
#出现次数最多的数
n = int(input())
a = list(map(int,input().split()))
b = list(set(a))#化为集合，去掉相同数
b.sort()#从小到大排序
s = dict(zip(b,map(a.count,b)))#将数与它的出现次数组合再转为字典
print(max(s,key=s.get))#根据字典值选出count最大的
