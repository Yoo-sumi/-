import copy
r,c,t=map(int,input().split())
graph=[]
robot=[]
for i in range(r):
    li=list(map(int,input().split()))
    graph.append(li)
    for j in range(c):
        if li[j]==-1:
            robot.append((i,j))
robot.sort()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(t):
    temp=[[0]*c for _ in range(r)]
    for x,y in robot:
        temp[x][y]=-1
    for i in range(r):
        for j in range(c):
            if graph[i][j]==0 or graph[i][j]==-1:
                continue
            count=0
            for index in range(4):
                nx=i+dx[index]
                ny=j+dy[index]
                if not 0<=nx<r or not 0<=ny<c:
                    continue
                if graph[nx][ny]==-1:
                    continue
                temp[nx][ny]+=graph[i][j]//5
                count+=1
            temp[i][j]+=graph[i][j]-(graph[i][j]//5)*count
    graph=copy.deepcopy(temp)

    #왼쪽
    before=graph[0][0]
    for i in range(1,robot[0][0]+1):
        graph[i][0],before=before,graph[i][0]
    print(graph)
    #아래
    for i in range(1,c):
        if robot[0][1]==i:
            before=0
            continue
        graph[robot[0][0]][i],before=before,graph[robot[0][0]][i]
    print(graph)
    #오른쪽
    for i in range(robot[0][0]-1,-1,-1):
        graph[i][c-1],before=before,graph[i][c-1]

    print(graph)
    #위쪽
    for i in range(c-2,-1,-1):
        graph[0][i],before= before,graph[0][i]

    print(graph)

    #위
    before=graph[robot[1][0]+1][0]
    for i in range(c):
        if robot[1][1]==i:
            before=0
            continue
        graph[robot[1][0]][i],before=before,graph[robot[1][0]][i]

    print(graph)
    #오른
    for i in range(robot[1][0]+1,r):
        graph[i][c-1],before=before,graph[i][c-1]

    print(graph)
    #아래
    for i in range(c-2,-1,-1):
        graph[r-1][i],before=before,graph[r-1][i]

    print(graph)
    #왼쪽
    for i in range(r-2,robot[1][0]-1,-1):
        graph[i][0],before=before,graph[i][0]
    print(graph)

print(graph)
