import sys
from collections import deque

input=sys.stdin.readline

m,n,h=map(int,input().split())
graph=[[[] for _ in range(n)] for _ in range(h)]
flag0=False
def pr(graph):
    for i in graph:
        for j in i:
            for hh in j:
                print(hh,end=" ")
            print()
        print()
    print()

for hh in range(h):
    for i in range(n):
        li=list(map(int,input().split()))
        for j in li:
            if j==0:
                flag0=True
            graph[hh][i].append(j)

if flag0==False:
    print(0)

dx=[0,0,0,0,1,-1]
dy=[0,0,-1,1,0,0]
dh=[-1,1,0,0,0,0]
q=deque()

def bfs(q):
    count=0
    while q:
        a=[]
        while q:
            now=q.popleft()
            for i in range(6):
                nh=now[0]+dh[i]
                nx=now[1]+dx[i]
                ny=now[2]+dy[i]
                if not 0<=nh<h or not 0<=nx<n or not 0<=ny<m:
                    continue
                if graph[nh][nx][ny]==-1:
                    continue
                if graph[nh][nx][ny]==0:
                    graph[nh][nx][ny]=1
                    a.append((nh,nx,ny))
        for i in a:
            q.append(i)
        count+=1
    return count-1
for hh in range(h):
    for i in range(n):
        for j in range(m):
            if graph[hh][i][j]==1:
                q.append((hh,i,j))
v=bfs(q)
flag=False

for i in graph:
    for j in i:
        if j.count(0)>0:
            flag=True
if flag==True:
    print(-1)
elif flag0==True:
    print(v)


