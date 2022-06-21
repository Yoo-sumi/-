
def biteFish(x,y,age):
    distance=[[0]*n for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    q=[]
    q.append((x,y))
    visited[x][y]=1
    temp=[]
    while q:
        now_x,now_y=q.pop(0)
        for i in range(4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if visited[nx][ny]==0:
                if graph[nx][ny]<=age:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    distance[nx][ny]=distance[now_x][now_y]+1
                    if graph[nx][ny]<age and graph[nx][ny]!=0:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x:(x[2],x[0],x[1]))

n=int(input())
graph=[]
shark_x,shark_y=-1,-1
shark_age=2
time=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]
for i in range(n):
    li=list(map(int,input().split()))
    for j in range(n):
        if li[j]==9:
            shark_x,shark_y=i,j
    graph.append(li)
graph[shark_x][shark_y]=0
count=0
while 1:
    shark=biteFish(shark_x,shark_y,shark_age)
    if len(shark)==0:
        break
    nx,ny,dis=shark[0][0],shark[0][1],shark[0][2]
    time+=dis
    graph[shark_x][shark_y],graph[nx][ny]=0,0
    shark_x,shark_y=nx,ny
    count+=1
    if count==shark_age:
        shark_age+=1
        count=0

print(time)