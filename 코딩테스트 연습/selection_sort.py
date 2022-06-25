arr=[6,3,8,5,2,7,4,1]
n=len(arr)
for i in range(n-1):
    index=i
    for j in range(i,n):
        if arr[index]>arr[j]:
            index=j
    arr[i],arr[index]=arr[index],arr[i]
    print(arr)
