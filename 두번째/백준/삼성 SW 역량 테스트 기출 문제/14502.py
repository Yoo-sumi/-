import sys
import copy
from itertools import combinations
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[] for _ in range(n)]
virus_location=[]
temp=copy.deepcopy(graph)
for i in range(n):
    graph[i]=list(map(int,input().split()))
    for j in range(m):
        if graph[i][j]==2:
            virus_location.append((i,j))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not 0<=nx<n or not 0<=ny<m:
            continue
        if temp[nx][ny]==0:
            temp[nx][ny]=2
            virus(nx,ny)

def score(array):
    v=0
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                v+=1
    return v

data=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            data.append((i,j))
lis=list(combinations(data,3))
result=0
for li in lis:
    temp=copy.deepcopy(graph)
    for a,b in li:
        temp[a][b]=1
    for a,b in virus_location:
        virus(a,b)
    result=max(result,score(temp))
print(result)



