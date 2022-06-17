import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
r,c,d=map(int,input().split())
for i in range(n):
    graph[i]=list(map(int,input().split()))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
trace=[(r,c)]
def change_direction(d):
    if d==0:
        return 3
    return d-1

while True:
    if graph[r][c]==0:
        graph[r][c]=-1
    flag=True
    for i in range(4):
        d=change_direction(d)
        nx=r+dx[d]
        ny=c+dy[d]
        if not 0<=nx<n or not 0<=ny<m:
            continue
        if graph[nx][ny]==0:
            r,c=nx,ny
            flag=False
            break
    if flag:
        nx=r-dx[d]
        ny=c-dy[d]
        if not 0<=nx<n or not 0<=ny<m:
            break
        if graph[nx][ny]==1:
            break
        r,c=nx,ny
result=0
for li in graph:
    result+=li.count(-1)
print(result)

