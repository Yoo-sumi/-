array=[]
def check(arr):
    count=0
    for i in range(5):
        if count==3:
            break
        if arr[i].count(-1)==5:
            count+=1

    for i in range(5):
        if count==3:
            break
        c=0
        for j in range(5):
            if arr[j][i]==-1:
                c+=1
        if c==5:
            count+=1
    c=0
    for j in range(5):
        if arr[j][j]==-1:
            c+=1
    if c==5:
        count+=1

    c=0
    for j in range(4,-1,-1):
        if arr[4-j][j]==-1:
            c+=1
    if c==5:
        count+=1

    if count>=3:
        return True
    return False
for _ in range(5):
    array.append(list(map(int,input().split())))
result=0
for z in range(5):
    li=list(map(int,input().split()))
    for i in range(5):
        for j in range(5):
            for h in range(5):
                if array[j][h]==li[i]:
                    array[j][h]=-1
        v=check(array)
        if v and result==0:
            result=z*5+(i+1)
print(result)
