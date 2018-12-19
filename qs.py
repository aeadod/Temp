def quick_sort(list1,left,right):
    if left>=right:
        return list1
    key=list1[left]
    low=left
    high=right
    while left!=right:
        while left<right and list1[right]>=key:
            right -=1
        list1[left]=list1[right]
        while left<right and list1[left]<=key:
            left +=1
        list1[right]=list1[left]
    list1[right]=key
    quick_sort(list1,low,left-1)
    quick_sort(list1,left+1,high)
    return list1
