import sys
input=sys.stdin.readline
n,m=map(int,input().split())
A=[]
cloud={}
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
cross=[1,3,5,7]
for _ in range(n):
    li=list(map(int,input().split()))
    A.append(li)
cloud[(n-1,0)],cloud[(n-1,1)],cloud[(n-2,0)],cloud[(n-2,1)]=1,1,1,1
for _ in range(m):
    d,s=map(int,input().split())
    d-=1
    temp=[]
    li=list(cloud.keys())
    for x,y in li:
        nx=(x+dx[d]*s)%n
        ny=(y+dy[d]*s)%n
        temp.append((nx,ny))
        del cloud[(x,y)]
        A[nx][ny]+=1
    for x,y in temp:
        c=0
        for index in cross:
            nx=x+dx[index]
            ny=y+dy[index]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if A[nx][ny]>0:
                c+=1
        A[x][y]+=c
    for i in range(n):
        for j in range(n):
            if A[i][j]>=2:
                if (i,j) in temp:
                    continue
                cloud[(i,j)]=1
                A[i][j]-=2
answer=0
for i in A:
    answer+=sum(i)
print(answer)




