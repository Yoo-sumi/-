def solution():
    n=int(input())
    arr=[]
    shark_x,shark_y=-1,-1
    shark_age=2
    fish=[]
    time=0
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    for i in range(n):
        li=list(map(int,input().split()))
        for j in range(n):
            if li[j]==9:
                shark_x,shark_y=i,j
            elif 1<=li[j]<=6:
                fish.append((i,j))
        arr.append(li)
    fish.sort(key=lambda x:(x[0],x[1]))
    arr[shark_x][shark_y]=0
    count=0
    while fish:
        print(shark_x,shark_y,shark_age,time)
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()
        x,y=-1,-1
        min_value=n*n
        for xx,yy in fish:
            if arr[xx][yy]>=shark_age:
                continue
            dis=abs(shark_x-xx)+abs(shark_y-yy)
            if dis<min_value:
                min_value=dis
                x,y=xx,yy
        if (x,y)==(-1,-1):
            break
        q=[]
        q.append((shark_x,shark_y,0,[]))
        res=n*n
        while q:
            s_x,s_y,di,foot=q.pop(0)
            if (s_x,s_y)==(x,y):
                for h_x,h_y in foot:
                    if 0<arr[h_x][h_y]<shark_age:
                        arr[h_x][h_y]=0
                        count+=1
                        fish.remove((h_x,h_y))
                    if count==shark_age:
                        shark_age+=1
                        count=0
                res=di
                break
            for i in range(4):
                nx=s_x+dx[i]
                ny=s_y+dy[i]
                if (nx,ny)==(shark_x,shark_y):
                    continue
                if not 0<=nx<n or not 0<=ny<n:
                    continue
                if arr[nx][ny]>shark_age:
                    continue
                if not (nx,ny) in foot:
                    q.append((nx,ny,di+1,foot+[(nx,ny)]))
        if res==n*n:
            break
        time+=res
        shark_x,shark_y=x,y
        arr[shark_x][shark_y]=0
        print(arr)
    return time
print(solution())
