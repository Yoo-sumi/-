n=int(input())
dic={}
step=[]
arr=[[0]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(1,n**2+1):
    li=list(map(int,input().split()))
    dic[li[0]]=li[1:]
    step.append(li[0])

for s in step:
    multi=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                continue
            c=0
            b=0
            for index in range(4):
                nx=i+dx[index]
                ny=j+dy[index]
                if not 0<=nx<n or not 0<=ny<n:
                    continue
                if arr[nx][ny] in dic[s]:
                    c+=1
                elif arr[nx][ny]==0:
                    b+=1
            multi.append((c,b,i,j))
    multi.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    arr[multi[0][2]][multi[0][3]]=s
answer=0
for i in range(n):
    for j in range(n):
        v=arr[i][j]
        c=0
        for index in range(4):
            nx=i+dx[index]
            ny=j+dy[index]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if arr[nx][ny] in dic[v]:
                c+=1
        if c<=1:
            answer+=c
        elif c==2:
            answer+=10
        elif c==3:
            answer+=100
        elif c==4:
            answer+=1000
print(answer)


