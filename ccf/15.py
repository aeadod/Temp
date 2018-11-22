x=int(input())

if x%50==0:
    c=int(x/10+x/50*2)

else :    
    if x//50>0:   
        c1=int((x-x%50)/10+(x-x%50)/50*2)
        if (x%50)%30==0:
            c2=int(x%50/10+x%50/30)
        else:
            if x%50==40:
                c2=5
            elif x%50==30:
                c2=4
            else :c2=int(x%50/10)
        c=c1+c2
    
    else:
        if x==40:
            c=5
        elif x==30:
            c=4
        else:
            c=int(x/10)

print(c)
