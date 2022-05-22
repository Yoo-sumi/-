from collections import deque
n,m,x,y,k=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))
move=list(map(int,input().split()))
box=[0,deque([0,0,0]),0,0]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def right():
    global box
    temp=box[3]
    box[3]=box[1].pop()
    box[1]=deque([temp])+box[1]
def left():
    global box
    temp=box[3]
    box[3]=box[1].popleft()
    box[1].append(temp)
def up():
    global box
    temp=[]
    for i in range(1,4):
        if i==1:
            temp.append(box[i][1])
        else:
            temp.append(box[i])
    box[3]=box[0]
    for i in range(len(temp)):
        if i==1:
            box[i][1]=temp[i]
        else:
            box[i]=temp[i]
def down():
    global box
    temp=[]
    for i in range(3):
        if i==1:
            temp.append(box[i][1])
        else:
            temp.append(box[i])
    box[0]=box[3]
    for i in range(1,1+len(temp)):
        if i==1:
            box[i][1]=temp[i-1]
        else:
            box[i]=temp[i-1]

for i in move:
    nx=x+dx[i-1]
    ny=y+dy[i-1]
    if not 0<=nx<n or not 0<=ny<m:
        continue
    if i==1:
        right()
    elif i==2:
        left()
    elif i==3:
        up()
    elif i==4:
        down()
    if graph[nx][ny]==0:
        graph[nx][ny]=box[3]
    else:
        box[3]=graph[nx][ny]
        graph[nx][ny]=0
    print(box[1][1])
    x,y=nx,ny

