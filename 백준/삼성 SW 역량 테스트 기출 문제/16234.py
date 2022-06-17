from collections import deque
n,l,r=map(int,input().split())
graph=[[] for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph[i]=list(map(int,input().split()))

def bfs(x,y,c):
    global array
    q=deque()
    total_count=0
    total_value=0
    q.append((x,y))
    trace=[]
    trace.append((x,y))
    array[x][y]=c
    while q:
        a,b=q.popleft()
        v=graph[a][b]
        total_count+=1
        total_value+=v
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if l<=abs(v-graph[nx][ny])<=r and array[nx][ny]==0:
                array[nx][ny]=c
                q.append((nx,ny))
                trace.append((nx,ny))
    for i,j in trace:
        graph[i][j]=total_value//total_count
result=0
while True:
    count=0
    array=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if array[i][j]==0:
                count+=1
                bfs(i,j,count)
    if count==n*n:
        break
    result+=1
print(result)




