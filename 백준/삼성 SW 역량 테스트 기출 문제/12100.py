import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))

q=deque()
q.append((array,0))
store=[]
def left(arr):
    global n
    temp=[[0]*n for _ in range(n)]
    stack=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                continue
            if len(stack[i])>0:
                if stack[i][-1][0]==arr[i][j] and stack[i][-1][1]==0:
                    stack[i].pop()
                    stack[i].append((arr[i][j]*2,1))
                    continue
            stack[i].append((arr[i][j],0))
    for i in range(n):
        for j in range(len(stack[i])):
            temp[i][j]=stack[i][j][0]
    return temp
def right(arr):
    global n
    temp=[[0]*n for _ in range(n)]
    stack=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr[i][j]==0:
                continue
            if len(stack[i])>0:
                if stack[i][-1][0]==arr[i][j] and stack[i][-1][1]==0:
                    stack[i].pop()
                    stack[i].append((arr[i][j]*2,1))
                    continue
            stack[i].append((arr[i][j],0))
    for i in range(n):
        for j in range(len(stack[i])):
            temp[i][n-1-j]=stack[i][j][0]
    return temp
def up(arr):
    global n
    temp=[[0]*n for _ in range(n)]
    stack=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[j][i]==0:
                continue
            if len(stack[i])>0:
                if stack[i][-1][0]==arr[j][i] and stack[i][-1][1]==0:
                    stack[i].pop()
                    stack[i].append((arr[j][i]*2,1))
                    continue
            stack[i].append((arr[j][i],0))
    for i in range(n):
        for j in range(len(stack[i])):
            temp[j][i]=stack[i][j][0]
    return temp
def down(arr):
    global n
    temp=[[0]*n for _ in range(n)]
    stack=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr[j][i]==0:
                continue
            if len(stack[i])>0:
                if stack[i][-1][0]==arr[j][i] and stack[i][-1][1]==0:
                    stack[i].pop()
                    stack[i].append((arr[j][i]*2,1))
                    continue
            stack[i].append((arr[j][i],0))
    for i in range(n):
        for j in range(len(stack[i])):
            temp[n-1-j][i]=stack[i][j][0]
    return temp

flag=True
while flag:
    temp=[]
    while q:
        array,count=q.popleft()
        arr_u=up(array)
        arr_d=down(array)
        arr_l=left(array)
        arr_r=right(array)
        if not (arr_u,count+1) in store:
            temp.append((arr_u,count+1))
            store.append((arr_u,count+1))
        if not (arr_d,count+1) in store:
            temp.append((arr_d,count+1))
            store.append((arr_d,count+1))
        if not (arr_l,count+1) in store:
            temp.append((arr_l,count+1))
            store.append((arr_l,count+1))
        if not (arr_r,count+1) in store:
            temp.append((arr_r,count+1))
            store.append((arr_r,count+1))
        if count==4:
            flag=False
    for i in temp:
        q.append(i)
result=0

while q:
    arr,c=q.popleft()
    maxx=0
    for i in range(n):
        maxx=max(maxx,max(arr[i]))
    result=max(result,maxx)

print(result)