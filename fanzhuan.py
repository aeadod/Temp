def fanzhuan(s):
    if s=='':
        return s
    else :
        return fanzhuan(s[1:])+s[0]
s='12345'
print(fanzhuan(s))
