from collections import deque
import copy
import sys
input=sys.stdin.readline
n,m,h=map(int,input().split())
graph=[[0]*n for _ in range(h)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

def move(arr):
    for ii in range(n):
        trace=[]
        x,y=0,ii
        trace.append((x,y))
        while x<h:
            ly=y-1
            lx=x
            if 0<=ly<n-1:
                if arr[lx][ly]==1:
                    if not (lx,ly) in trace:
                        x,y=lx,ly
                        trace.append((x,y))
                        continue
            rx,ry=x,y
            if 0<=ry<n-1:
                if arr[rx][ry]==1:
                    nx,ny=rx,ry+1
                    if not (nx,ny) in trace:
                        x,y=nx,ny
                        trace.append((x,y))
                        continue
            nx=x+1
            ny=y
            if not (nx,ny) in trace:
                x,y=nx,ny
                trace.append((x,y))
        if ii!=y:
            return False
    return True
def add(x,y,arr):
    if y==n-1:
        return False
    if y==0:
        if arr[x][y+1]==0:
            return True
    if y==n-2:
        if arr[x][y-1]==0:
            return True

    if arr[x][y+1]==0 and arr[x][y-1]==0:
        return True
    else:
        return False
q=deque()
blank=[]
for i in range(h):
    for j in range(n):
        if graph[i][j]==0:
            blank.append((i,j))
q.append((graph,0,blank))
result=1e9

def bfs():
    while q:
        aa=[]
        while q:
            now,count,bla=q.popleft()
            if move(now):
                return count
            if count==3:
                continue
            for a,b in bla:
                if add(a,b,now):
                    bla.remove((a,b))
                    temp=copy.deepcopy(now)
                    temp[a][b]=1
                    aa.append((temp,count+1,bla))
                    bla.append((a,b))
        for ii in aa:
            if move(ii[0]):
                return ii[1]
            q.append(ii)
    return -1
print(bfs())