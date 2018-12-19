def bubble_sort(list1):
    n=len(list1)
    if n==0:
        return 'empty'
    elif n==1:
        return list1
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if list1[i]>list1[j]:
                    list1[i],list1[j]=list1[j],list1[i]
    return list1
