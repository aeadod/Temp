tempstr=input('shuru:')
if tempstr[-1] in ['F','f']:
    c=(eval(tempstr[0:-1])-32)/1.8
    print("{:.2f}C".format(c))
elif tempstr[-1] in ['c','C']:
    f=eval(tempstr[0:-1])*1.8+32
    print("{:.2f}F".format(f))
