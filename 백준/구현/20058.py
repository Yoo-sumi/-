import sys
input=sys.stdin.readline
n,q=map(int,input().split())
A=[]
#A=[[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
for i in range(2**n):
    A.append(list(map(int,input().split())))
def rotate(arr,start,end):
    start_x,start_y=start[0],start[1]
    end_x,end_y=end[0],end[1]
    h=end_x-start_x+1
    temp=[[] for _ in range(h)]
    index=0
    for i in range(start_y,end_y+1):
        for j in range(start_x+h-1,-1,-1):
            temp[index].append(arr[j][i])
        index+=1
    for i in range(h):
        for j in range(h):
            arr[i+start_x][j+start_y]=temp[i][j]
    return arr
dx=[-1,1,0,0]
dy=[0,0,-1,1]
Q=list(map(int,input().split()))
for l in Q:
    for i in range(0,len(A[0]),2**l):
        for j in range(0,len(A[0]),2**l):
            A=rotate(A,(i,j),((i+2**l)-1,(j+2**l)-1))
    temp=set()
    for i in range(2**n):
        for j in range(2**n):
            if A[i][j]==0:
                continue
            c=0
            for index in range(4):
                nx=i+dx[index]
                ny=j+dy[index]
                if 0<=nx<2**n and 0<=ny<2**n:
                    if A[nx][ny]>0:
                        c+=1
            if c<3:
                temp.add((i,j))
    for x,y in temp:
        A[x][y]-=1
flag=[[0]*(2**n) for _ in range(2**n)]
answer=0
block=0
def bfs(x,y,count):
    global flag,A,answer,block
    q=[]
    b=0
    q.append((x,y))
    flag[x][y]=count
    b+=1

    while q:
        now_x,now_y=q.pop(0)
        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if 0<=nx<len(flag) and 0<=ny<len(flag[0]):
                if A[nx][ny]>0 and flag[nx][ny]==0:
                    q.append((nx,ny))
                    flag[nx][ny]=count
                    b+=1
    block=max(block,b)
count=1
for i in range(2**n):
    for j in range(2**n):
        answer+=A[i][j]
        if flag[i][j]==0 and A[i][j]>0:
            bfs(i,j,count)
            count+=1
print(answer)
print(block)