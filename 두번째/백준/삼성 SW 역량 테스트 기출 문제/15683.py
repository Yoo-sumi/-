from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
camera=[]
for i in range(n):
    li=list(map(int,input().split()))
    for j in range(m):
        if 1<=li[j]<=5:
            camera.append((i,j))
    graph[i]=li
q=deque()
q.append((graph,camera))
def copy_arr(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j]=arr[i][j]
    return temp
def one_1(x,y,arr):
    temp=copy_arr(arr)
    #오른
    for i in range(y+1,m):
        if temp[x][i]==6:
            break
        if temp[x][i]==0:
            temp[x][i]='#'
    return temp
def one_2(x,y,arr):
    temp=copy_arr(arr)
    #down
    for i in range(x+1,n):
        if temp[i][y]==6:
            break
        if temp[i][y]==0:
            temp[i][y]='#'
    return temp
def one_3(x,y,arr):
    temp=copy_arr(arr)
    #왼
    for i in range(y-1,-1,-1):
        if temp[x][i]==6:
            break
        if temp[x][i]==0:
            temp[x][i]='#'
    return temp
def one_4(x,y,arr):
    temp=copy_arr(arr)
    #up
    for i in range(x-1,-1,-1):
        if temp[i][y]==6:
            break
        if temp[i][y]==0:
            temp[i][y]='#'
    return temp
def two_1(x,y,arr):
    temp=copy_arr(arr)
    temp=one_3(x,y,temp)
    temp=one_1(x,y,temp)
    return temp
def two_2(x,y,arr):
    temp=copy_arr(arr)
    temp=one_4(x,y,temp)
    temp=one_2(x,y,temp)
    return temp

def three_1(x,y,arr):
    temp=copy_arr(arr)
    temp=one_4(x,y,temp)
    temp=one_1(x,y,temp)
    return temp
def three_2(x,y,arr):
    temp=copy_arr(arr)
    temp=one_1(x,y,temp)
    temp=one_2(x,y,temp)
    return temp
def three_3(x,y,arr):
    temp=copy_arr(arr)
    temp=one_2(x,y,temp)
    temp=one_3(x,y,temp)
    return temp
def three_4(x,y,arr):
    temp=copy_arr(arr)
    temp=one_3(x,y,temp)
    temp=one_4(x,y,temp)
    return temp
def four_1(x,y,arr):
    temp=copy_arr(arr)
    temp=one_4(x,y,temp)
    temp=one_1(x,y,temp)
    temp=one_2(x,y,temp)
    return temp
def four_2(x,y,arr):
    temp=copy_arr(arr)
    temp=one_1(x,y,temp)
    temp=one_2(x,y,temp)
    temp=one_3(x,y,temp)
    return temp
def four_3(x,y,arr):
    temp=copy_arr(arr)
    temp=one_2(x,y,temp)
    temp=one_3(x,y,temp)
    temp=one_4(x,y,temp)
    return temp
def four_4(x,y,arr):
    temp=copy_arr(arr)
    temp=one_3(x,y,temp)
    temp=one_4(x,y,temp)
    temp=one_1(x,y,temp)
    return temp
def five(x,y,arr):
    temp=copy_arr(arr)
    temp=one_1(x,y,temp)
    temp=one_2(x,y,temp)
    temp=one_3(x,y,temp)
    temp=one_4(x,y,temp)
    return temp
def score(arr):
    total=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                total+=1
    return total
result=n*m
while q:
    t=[]
    cam=q[-1][1]
    if len(cam)==0:
        now,cam=q.popleft()
        result=min(result,score(now))
        continue
    x,y=cam.pop()
    while q:
        now,cam=q.popleft()
        if now[x][y]==1:
            t.append((one_1(x,y,now),cam))
            t.append((one_2(x,y,now),cam))
            t.append((one_3(x,y,now),cam))
            t.append((one_4(x,y,now),cam))
        elif now[x][y]==2:
            t.append((two_1(x,y,now),cam))
            t.append((two_2(x,y,now),cam))
        elif now[x][y]==3:
            t.append((three_1(x,y,now),cam))
            t.append((three_2(x,y,now),cam))
            t.append((three_3(x,y,now),cam))
            t.append((three_4(x,y,now),cam))
        elif now[x][y]==4:
            t.append((four_1(x,y,now),cam))
            t.append((four_2(x,y,now),cam))
            t.append((four_3(x,y,now),cam))
            t.append((four_4(x,y,now),cam))
        elif now[x][y]==5:
            t.append((five(x,y,now),cam))
    for xx in t:
        q.append(xx)
print(result)




