import copy
import sys
input=sys.stdin.readline
from itertools import combinations

n,m=map(int,input().split())
arr=[]
virus=[]
ff=False
for i in range(n):
    li=list(map(int,input().split()))
    arr.append(li)
    for j in range(n):
        if li[j]==2:
            virus.append((i,j))
        if li[j]==0:
            ff=True
#3을 활성 바이러스로 정함.
def move(arr,vi):
    global n
    c=False
    temp=copy.deepcopy(arr)
    ll=copy.deepcopy(vi)
    for i,j in vi:
        for index in range(4):
            nx=i+dx[index]
            ny=j+dy[index]
            if not 0<=nx<n or not 0<=ny<n:
                continue
            if arr[nx][ny]==2:
                temp[nx][ny]=3
            elif arr[nx][ny]==0:
                if not (nx,ny) in vi:
                    temp[nx][ny]=3
                    ll.append((nx,ny))
                    c=True
    return [temp,c,ll]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

if ff==False:
    print(0)
else:
    li=list(combinations(virus,m))
    answer=1e9
    for i in li:
        arr2=copy.deepcopy(arr)
        vivi=list(i)
        for x,y in i:
            arr2[x][y]=3
        time=1
        before=1e9
        while True:
            arr2,f,vivi=move(arr2,vivi)
            if f==False:
                break
            c=0
            for ii in arr2:
                for jj in ii:
                    if jj==0:
                        c+=1
            if c==0:
                answer=min(answer,time)
                break
            time+=1
    if answer==1e9:
        print(-1)
    else:
        print(answer)