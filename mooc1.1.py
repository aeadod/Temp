tempstr=input('shuru:')
if tempstr[0] in ['F','f']:
    c=(eval(tempstr[1:])-32)/1.8
    print("{:.2f}C".format(c))
elif tempstr[0] in ['c','C']:
    f=eval(tempstr[0:])*1.8+32
    print("{:.2f}F".format(f))
