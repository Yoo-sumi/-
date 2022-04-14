import sys
import copy
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
state=[[0]*m for _ in range(n)]
q=deque()
def pr(a):
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=" ")
        print()
    print()
for i in range(n):
        li=list(input())
        for j in range(m):
            graph[i].append(int(li[j]))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def solution(x,y):
    array=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j]=graph[i][j]
    array[x][y]=0
    array[0][0]=-1
    q.append((0,0,0))
    while q:
        now=q.popleft()
        print(now)
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            v=now[2]
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if array[nx][ny]==1 and now[2]==0:
                array[nx][ny]=0
                state[nx][ny]=1
                v=1
            if array[nx][ny]==0:
                array[nx][ny]=array[now[0]][now[1]]-1
                q.append((nx,ny,v))
        pr(array)
    return -array[n-1][m-1]


result=solution(0,0)

if result==0:
    print(-1)
else:
    print(result)
