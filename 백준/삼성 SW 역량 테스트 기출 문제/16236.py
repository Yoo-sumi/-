from collections import deque
n=int(input())
graph=[[] for _ in range(n)]
q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
flag=[]
count=0
age=9
for i in range(n):
    li=list(map(int,input().split()))
    for j in range(len(li)):
        if li[j]==9:
            q.append((i,j))
            flag.append((i,j))
        if 1<=li[j]<=6:
            count+=1
    graph[i]=li
time=0
graph[q[0][0]][q[0][1]]=0
while q:
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end=" ")
        print()
    print()
    x,y=q.popleft()
    if 1<=graph[x][y]<=6:
        count-=1
    print(x,y)
    eat_arr=[]
    same_arr=[]
    zero_arr=[]
    same_count=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not 0<=nx<n or not 0<=ny<n:
            continue
        if graph[nx][ny]>age:
            continue
        #eat
        if graph[nx][ny]<age and graph[nx][ny]!=0:
            eat_arr.append((abs(x-nx)+abs(y-ny),nx,ny))
        #same
        elif graph[nx][ny]==age:
            same_arr.append((abs(x-nx)+abs(y-ny),nx,ny))
        elif graph[nx][ny]==0:
            zero_arr.append((abs(x-nx)+abs(y-ny),nx,ny))
    eat_arr.sort(key=lambda x:(x[0],x[1],x[2]))
    same_arr.sort(key=lambda x:(x[0],x[1],x[2]))
    print(eat_arr,same_arr,zero_arr)
    if eat_arr:
        f=False
        for a in eat_arr:
            if not (a[1],a[2]) in flag:
                q.append((a[1],a[2]))
                flag.append((a[1],a[2]))
                if age==graph[a[1]][a[2]]:
                    age+=1
                graph[a[1]][a[2]]=0
                time+=1
                f=True
                break
        if f:
            continue
    if same_arr:
        f=False
        for a in same_arr:
            if not (a[1],a[2]) in flag:
                q.append((a[1],a[2]))
                flag.append((a[1],a[2]))
                time+=1
                f=True
                break
        if f:
            continue
    if count==0:
        print(count)
        break
    if zero_arr:
        f=False
        for a in zero_arr:
            if not (a[1],a[2]) in flag:
                q.append((a[1],a[2]))
                flag.append((a[1],a[2]))
                time+=1
                f=True
                break
        if f:
            continue
    if not eat_arr and not same_arr and not zero_arr:
        break
print(time)