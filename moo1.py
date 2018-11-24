x=input()
if x[-1]=='c' or x[-1]=='C':
    x=(x[:-1])
    print("%.2f F"% (int(x)*1.8+32))
elif x[-1]=='f' or x[-1]=='F':
    x=(x[:-1])
    print("%.2f C"% ((int(x)-32)/8))
