zero,one=0,0
def dfs(arr,row,col):
    global zero,one
    n=row[1]-row[0] #size
    if n==1:
        if arr[row[0]][col[0]]==0:
            zero+=1
        elif arr[row[0]][col[0]]==1:
            one+=1
        return
    num=arr[row[0]][col[0]]
    flag=False
    for i in range(row[0],row[1]):
        for j in range(col[0],col[1]):
            if arr[i][j]!=num:
                flag=True
                break
        if flag:
            break
    if flag==False:
        if arr[row[0]][col[0]]==0:
            zero+=1
        elif arr[row[0]][col[0]]==1:
            one+=1
        return
    nrow1=(row[0],row[0]+(n//2))
    ncol1=(col[0],col[0]+(n//2))
    nrow2=(row[0]+(n//2),row[1])
    ncol2=(col[0]+(n//2),col[1])
    dfs(arr,nrow1,ncol1)
    dfs(arr,nrow1,ncol2)
    dfs(arr,nrow2,ncol1)
    dfs(arr,nrow2,ncol2)

def solution(arr):
    dfs(arr,(0,len(arr)),(0,len(arr)))
    return [zero,one]