alist=list(map(int ,input().split()))
score=0
flag=1
for i in range(len(alist)):
    if alist[i]==1:
        score+=1
        
        
    elif alist[i]==0:
        break;
    elif alist[i]==2:
        score=score+2*flag
        flag+=1
        if alist[i+1]!=2:
            flag=1
print(score)
        
        
