n,m,k=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
map1=[2,1,5,6]
map2=[4,1,3]
d=3
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def change_dir(num):
    global d
    #반대
    if num==1:
        d=(d+2)%4
    #시
    elif num==2:
        d=(d-1)%4
    #반시계
    elif num==3:
        d=(d+1)%4
def rotate_map(num):
    global map1,map2
    #right
    if num==3:
        map2,map1[-1]=[map1[-1]]+map2[:-1],map2[-1]
        map1[1]=map2[1]
    #left
    elif num==1:
        map2,map1[-1]=map2[1:]+[map1[-1]],map2[0]
        map1[1]=map2[1]
    #up
    elif num==0:
        map1=map1[1:]+[map1[0]]
        map2[1]=map1[1]
    #down
    elif num==2:
        map1=[map1[-1]]+map1[:-1]
        map2[1]=map1[1]
def bfs(x,y,num):
    global arr
    q=[]
    q.append((x,y))
    flag=[[False]*m for _ in range(n)]
    flag[x][y]=True
    count=0
    while q:
        now_x,now_y=q.pop(0)
        count+=1
        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if flag[nx][ny]==False and arr[nx][ny]==num:
                q.append((nx,ny))
                flag[nx][ny]=True
    return count
x,y=0,0
answer=0
for _ in range(k):
    nx=x+dx[d]
    ny=y+dy[d]
    if not 0<=nx<n or not 0<=ny<m:
        change_dir(1)
        nx=x+dx[d]
        ny=y+dy[d]
    rotate_map(d)
    x,y=nx,ny
    #2
    b=arr[x][y]
    c=bfs(x,y,b)
    answer+=(b*c)
    #3
    if map1[-1]>b:
        change_dir(2)
    elif map1[-1]<b:
        change_dir(3)
print(answer)


