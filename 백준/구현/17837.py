n,k=map(int,input().split())
arr=[]
dic={}
dx=[0,0,-1,1]
dy=[1,-1,0,0]
index=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(k):
    x,y,c=map(int,input().split())
    x,y,c=x-1,y-1,c-1
    dic[(x,y)]=dic.get((x,y),[])+[i]
    index.append((x,y,c))

#move
for i in range(len(k)):
    x,y,c=index[i]
    nx=x+dx[c]
    ny=y+dy[c]
    if not 0<=nx<n or not 0<=ny<n:
        c=(c+2)%4
        index[i][2]=c
        nx=x+dx[c]
        ny=y+dy[c]
        if arr[nx][ny]==2:
            continue
        x,y=nx,ny

    if arr[nx][ny]==2:
        c=(c+2)%4
        index[i][2]=c
        nx=x+dx[c]
        ny=y+dy[c]
        if arr[nx][ny]==2:
            continue
    elif arr[nx][ny]==0:
        if (nx,ny) in dic.keys():
            x,y=nx,ny

