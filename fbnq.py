def fbnq(x):
    if x==1 or x== 2:
        return 1
    else :
        return fbnq(x-1)+fbnq(x-2)
print(fbnq(5))
