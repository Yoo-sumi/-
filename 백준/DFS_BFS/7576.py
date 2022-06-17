import sys
from collections import deque

input=sys.stdin.readline

m,n=map(int,input().split())
graph=[[] for _ in range(n)]
flag0=False
for i in range(n):
    li=list(map(int,input().split()))
    for j in li:
        if j==0:
            flag0=True
        graph[i].append(j)
if flag0==False:
    print(0)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
def pr(graph):
    for i in graph:
        for j in i:
            print(j,end=" ")
        print()
    print()
def bfs(q):
    count=0
    while q:
        a=[]
        while q:
            now=q.popleft()
            for i in range(4):
                nx=now[0]+dx[i]
                ny=now[1]+dy[i]
                if not 0<=nx<n or not 0<=ny<m:
                    continue
                if graph[nx][ny]==-1:
                    continue
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    a.append((nx,ny))
        for i in a:
            q.append(i)
        count+=1
    return count-1
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))
v=bfs(q)
flag=False
for i in graph:
    if i.count(0)>0:
        flag=True
if flag==True:
    print(-1)
elif flag0==True:
    print(v)


