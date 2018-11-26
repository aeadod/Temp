def getchar():
    txt=open(r'C:\Users\aeado\Desktop\123456.txt','r').read()
    txt=txt.lower()
    for ch in '~!@#$%^&*()_+-=`[]\;,./{}|:"<>?\'':
        txt=txt.replace(ch,' ')
    return txt
import sanguo
hamlet=getchar()
words=hamlet.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=1)
for i in range(20):
    word,count=items[i]
    print("{:<10}{:>5}".format(word,count))
