def paint(arr,r,c):
    for i in range(r):
        for j in range(c):
            if arr[i][j]==-1:
                print('.',end="")
            else:
                print('O',end="")
        print()
def solution():
    r,c,n=map(int,input().split())
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    arr=[[-1]*c for _ in range(r)]
    for i in range(r):
        li=list(map(str,input()))
        for j in range(len(li)):
            if li[j]=='O':
                arr[i][j]=2

    if n==1:
        return paint(arr,r,c)
    time=2
    while time<=n:
        if time%2==0:
            for i in range(r):
                for j in range(c):
                    if arr[i][j]==-1:
                        arr[i][j]=3
                    else:
                        arr[i][j]-=1
        else:
            temp=[]
            for i in range(r):
                for j in range(c):
                    if arr[i][j]>1:
                        arr[i][j]-=1
                    elif arr[i][j]==1:
                        temp.append((i,j))
                        for h in range(4):
                            nx=i+dx[h]
                            ny=j+dy[h]
                            if not 0<=nx<r or not 0<=ny<c:
                                continue
                            temp.append((nx,ny))
            for a,b in temp:
                arr[a][b]=-1
        time+=1
    paint(arr,r,c)
solution()
