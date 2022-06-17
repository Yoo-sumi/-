import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
q=deque()

for i in range(n):
    array=list(input())
    for j in range(m):
        graph[i].append(int(array[j]))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q.append((x,y))
    while q:
        now=q.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]+=graph[now[0]][now[1]]
                q.append((nx,ny))



bfs(0,0)
print(graph[n-1][m-1])