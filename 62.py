
a=input()
b=''.join(a.split('-'))
total=0

for i in range(len(b)-1):
    total+=int(b[i])*(i+1)


if b[len(b)-1]=='X':
    
    if total%11==10:
        print('Right')
    else:
        #print(b[0]+'-'+b[1:4]+'-'+b[4:9]+'-'+'X')
        print(b[0]+'-'+b[1:4]+'-'+b[4:9]+'-'+'{}'.format(total%11))

   

elif b[len(b)-1]!='X':
    if int(b[len(b)-1])==(total%11):
        print('Right')
    elif total%11==10:
        print(b[0]+'-'+b[1:4]+'-'+b[4:9]+'-'+'X')

    else:
    
    
        print(b[0]+'-'+b[1:4]+'-'+b[4:9]+'-'+'{}'.format(total%11))
