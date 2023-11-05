def selectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        minIdx=i
        for j in range (i+1,n):
            if arr[j]<arr[minIdx]:
                minIdx=j
        arr[i],arr[minIdx]=arr[minIdx],arr[i]
            
arr=[4,5,8,0,1,2,3]
selectionSort(arr)
print(arr)
