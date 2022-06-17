import sys
from collections import deque
input=sys.stdin.readline
n,m,k=map(int,input().split())
food=[[5]*n for _ in range(n)]
food_data=[]
graph=[[deque() for _ in range(n)] for _ in range(n)]

dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]
for _ in range(n):
    food_data.append(list(map(int,input().split())))
for _ in range(m):
    x,y,z=map(int,input().split())
    x-=1
    y-=1
    graph[x][y].append(z)

for _ in range(k):
    #봄 #여름
    for i in range(n):
        for j in range(n):
            li=graph[i][j]
            temp=deque()
            for h in range(len(li)):
                if food[i][j]-li[h]<0:
                    for kk in range(h,len(li)):
                        food[i][j]+=li[kk]//2
                    break
                food[i][j]-=li[h]
                temp.append(li[h]+1)
            graph[i][j]=temp
    #가을
    for i in range(n):
        for j in range(n):
            li=graph[i][j]
            for h in range(len(li)):
                if li[h]%5==0:
                    for d in range(8):
                        nx=i+dx[d]
                        ny=j+dy[d]
                        if not 0<=nx<n or not 0<=ny<n:
                            continue
                        graph[nx][ny].appendleft(1)
    #겨울
    for i in range(n):
        for j in range(n):
            food[i][j]+=food_data[i][j]


result=0
for i in range(n):
    for j in range(n):
        result+=len(graph[i][j])

print(result)

