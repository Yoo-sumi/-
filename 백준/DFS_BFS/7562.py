import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
result=[]

dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]

def pr(graph):
    for i in graph:
        for j in i:
            print(j,end=" ")
        print()
    print()

def bfs(graph,l,start,end):
    q=deque()
    q.append((start[0],start[1]))

    while q:
        now_x,now_y=q.popleft()
        if now_x==end[0] and now_y==end[1]:
            return graph[now_x][now_y]
        for i in range(8):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if not 0<=nx<l or not 0<=ny<l:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[now_x][now_y]+1
                q.append((nx,ny))
    return -1

for _ in range(t):
    l=int(input())
    graph=[[0]*l for _ in range(l)]
    start_x,start_y=map(int,input().split())
    end_x,end_y=map(int,input().split())
    result.append(bfs(graph,l,[start_x,start_y],[end_x,end_y]))

for i in result:
    print(i)