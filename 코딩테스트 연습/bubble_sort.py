arr=[5,1,6,2,4,3]
for i in range(len(arr)-1):
    flag=True
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            flag=False
            arr[j],arr[j+1]=arr[j+1],arr[j]
    if flag:
        break
    print(arr)
