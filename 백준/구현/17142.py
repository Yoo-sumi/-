import copy
from itertools import combinations
n,m=map(int,input().split())
arr=[]
virus=[]
'''for i in range(n):
    li=list(map(int,input().split()))
    arr.append(li)
    for j in range(n):
        if li[j]==2:
            virus.append((i,j))'''
#print(arr)
arr=[[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 2]]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
#3을 활성 바이러스로 정함.
def move(arr,time):
    global n
    temp=copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]==3:
                for index in range(4):
                    nx=i+dx[index]
                    ny=j+dy[index]
                    if not 0<=nx<n or not 0<=ny<n:
                        continue
                    if arr[nx][ny]==2:
                        temp[nx][ny]=3
                    elif arr[nx][ny]<=0:
                        temp[nx][ny]=-time
    print(temp)
    return temp
virus=[(0,0),(1,5),(4,3),(6,0),(6,6)]
li=list(combinations(virus,3))
answer=1e9
for i in li:
    arr2=copy.deepcopy(arr)
    for x,y in i:
        arr2[x][y]=3
    time=1
    before=1e9
    while True:
        arr2=move(arr2,time)
        c=0
        for ii in arr2:
            for jj in ii:
                if jj==0:
                    c+=1
        if c==0:
            answer=min(answer,time)
            break
        if before==c:
            answer=-1
            break
        time+=1
        before=c
print(answer)