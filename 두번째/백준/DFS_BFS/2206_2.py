import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[[[0]*m for _ in range(n)] for _ in range(2)]
q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def pr(graph):
    for i in graph:
        for j in i:
            for h in j:
                print(h,end=" ")
            print()
        print()
    print()

for i in range(n):
    li=list(input())
    for j in range(m):
        graph[i].append(int(li[j]))

def bfs():
    visited[0][0][0]=1
    q.append((0,0,0))

    while q:
        w,x,y=q.popleft()
        if x==n-1 and y==m-1:
            return visited[w][x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if graph[nx][ny]==1 and w==0:
                visited[1][nx][ny]=visited[w][x][y]+1
                q.append((1,nx,ny))
            elif graph[nx][ny]==0 and visited[w][nx][ny]==0:
                visited[w][nx][ny]=visited[w][x][y]+1
                q.append((w,nx,ny))
    return -1

print(bfs())
