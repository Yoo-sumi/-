import math
n=int(input())
result=[]
graph=[[0]*101 for _ in range(101)]
array=[]
def paint(start,g):
    global array
    for c in range(g):
        far=array[-1]
        temp=[]
        for a,b in array[::-1]:
            if (a,b)==far:
                continue
            xx=far[0]-a
            yy=far[1]-b
            nx,ny=far[0],far[1]
            #위->오
            if xx>0:
                ny+=abs(xx)
            #아래->왼
            elif xx<0:
                ny-=abs(xx)
            #왼->위
            if yy>0:
                nx-=abs(yy)
            #오른->아래
            elif yy<0:
                nx+=abs(yy)
            if not 0<=nx<101 or not 0<=ny<101:
                continue
            temp.append((nx,ny))
        for i in temp:
            if not i in array:
                array.append(i)
    return array


for i in range(n):
    array=[]
    y,x,d,g=map(int,input().split())
    if d==0:
        nx,ny=x,y+1
    elif d==1:
        nx,ny=x-1,y
    elif d==2:
        nx,ny=x,y-1
    elif d==3:
        nx,ny=x+1,y
    if not 0<=nx<101 or not 0<=ny<101:
        continue
    array.append((x,y))
    array.append((nx,ny))
    arr=paint((x,y),g)
    for j in arr:
        if not j in result:
            result.append(j)
            graph[j[0]][j[1]]=1
count=0
for i in range(100):
    for j in range(100):
        if graph[i][j]==graph[i+1][j]==graph[i][j+1]==graph[i+1][j+1]==1:
            count+=1
print(count)