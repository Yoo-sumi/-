from collections import deque
def solution(maps):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    q=deque()
    q.append((0,0))
    n=len(maps)
    m=len(maps[0])
    print(n,m)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not 0<=nx<n or not 0<=ny<m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
    if maps[n-1][m-1]==1:
        return -1
    return maps[n-1][m-1]