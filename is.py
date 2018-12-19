def insert_sort(list1):
    n=len(list1)
    if n == 0:
        return 'empty'
    elif n == 1:
        return  list1
    else :
        for i in range(1,n):
            key=list1[i]
            j=i-1
            while j >= 0:
                if list1[j]>key:
                    list1[j+1]=list1[j]
                    list1[j]=key
                j-=1
    return list1
