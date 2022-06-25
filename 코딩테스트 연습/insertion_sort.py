arr=[8,5,6,2,4]
n=len(arr)
for i in range(1,n):
    index=i
    for j in range(i-1,-1,-1):
        if arr[index]<arr[j]:
            arr[index],arr[j]=arr[j],arr[index]
            index=j
        else:
            break
    print(arr)
