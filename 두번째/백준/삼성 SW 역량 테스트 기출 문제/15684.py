from collections import deque
import copy
import sys
input=sys.stdin.readline
n,m,h=map(int,input().split())
graph=[[0]*n for _ in range(h)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

def move(arr,start):
    trace=[]
    x,y=0,start
    trace.append((x,y))
    while x<h:
        #left
        if y!=0:
            nx,ny=x,y
            if arr[x][y-1]==1:
                ny-=1
                if not (nx,ny) in trace:
                    x,y=nx,ny
                else:
                    x+=1
                trace.append((x,y))
                continue
        #right
        if y<n-1:
            nx,ny=x,y
            if arr[x][y]==1:
                ny+=1
                if not (nx,ny) in trace:
                    x,y=nx,ny
                else:
                    x+=1
                trace.append((x,y))
                continue
        nx=x+1
        ny=y
        if not (nx,ny) in trace:
            x,y=nx,ny
        else:
            x+=1
        trace.append((x,y))
    return y
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

q.append((graph,0))
result=1e9
def p(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print()
while q:
    now,count=q.popleft()
    v=[]
    for i in range(n):
        v.append(move(now,i))
    flag=True
    for i in range(n):
        if i!=v[i]:
            flag=False
    if flag:
        result=count
        break
    if count==3:
        continue
    for i in range(h):
        for j in range(n):
            if now[i][j]==0:
                if add(i,j,now):
                    temp=copy.deepcopy(now)
                    temp[i][j]=1
                    q.append((temp,count+1))
if result!=1e9:
    print(result)
else:
    print(-1)