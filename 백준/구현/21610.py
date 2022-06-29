n,m=map(int,input().split())
A=[]
cloud={}
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
cross=[1,3,5,7]
for _ in range(n):
    li=list(map(int,input().split()))
    A.append(li)
for _ in range(m):
    d,s=map(int,input().split())
    d-=1
    cloud[(n-1,0)],cloud[(n-1,1)],cloud[(n-2,0)],cloud[(n-2,1)]=1,1,1,1
    temp=[]
    li=list(cloud.keys())
    for x,y in li:
        # 이부분 다시 짜기
        nx=x+(dx[d]*s)
        ny=y+(dy[d]*s)
        print(nx,ny)
        if nx<0:
            v=nx%n
            nx=n-abs(v)
        elif nx>=n:
            v=nx%n
            nx=v
        if ny<0:
            v=ny%n
            ny=n-abs(v)
        elif ny>=n:
            v=nx%n
            ny=v
        temp.append((nx,ny))
        del cloud[(x,y)]
        print(x,y,nx,ny)
        A[nx][ny]+=1
    for i in range(n):
        for j in range(n):
            c=0
            for index in cross:
                nx=i+dx[index]
                ny=j+dy[index]
                if not 0<=nx<n or not 0<=ny<n:
                    continue
                if A[nx][ny]>0:
                    c+=1
            A[i][j]+=c
            if (i,j) in temp:
                continue
            if A[i][j]>=2:
                cloud[(i,j)]=1
                A[i][j]-=2
answer=0
for i in A:
    for j in i:
        answer+=1
print(answer)




