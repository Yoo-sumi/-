from collections import deque
n=int(input())
k=int(input())
graph=[[0]*n for _ in range(n)]
for _ in range(k):
    x,y=map(int,input().split())
    graph[x-1][y-1]=1
l=int(input())
move=[]
snack=deque()
for _ in range(l):
    a,b=map(str,input().split())
    move.append((int(a),b))
move.reverse()

time=0
dx=[-1,0,1,0]
dy=[0,-1,0,1]
direction=3
def change_direction(s):
    global direction
    if s=='L':
        if direction==3:
            direction=0
        else:
            direction+=1
    elif s=='D':
        if direction==0:
            direction=3
        else:
            direction-=1

snack.append((0,0))
x,y=(0,0)

while True:
    time+=1
    nx=x+dx[direction]
    ny=y+dy[direction]
    if not 0<=nx<n or not 0<=ny<n:
        break
    if (nx,ny) in snack:
        break
    if graph[nx][ny]==0:
        snack.popleft()
    elif graph[nx][ny]==1:
        graph[nx][ny]=0
    snack.append((nx,ny))
    x,y=nx,ny
    if len(move)>0:
        if move[-1][0]==time:
            m=move.pop()
            change_direction(m[1])
print(time)