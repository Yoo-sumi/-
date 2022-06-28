import copy
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
li=list(map(int,input().split()))
arr=[]
arr.append(li[:n])
arr.append(list(reversed(li[n:])))
robot=[0]*n
answer=0
while True:
    answer+=1
    #1 rotate
    up=arr[1][0]
    down=arr[0].pop()
    arr[0]=[up]+arr[0]
    arr[1]=arr[1][1:]+[down]
    '''temp=[[0]*n for _ in range(2)]
    for i in range(1,n):
        temp[0][i]=arr[0][i-1]
    temp[1][n-1]=arr[0][n-1]
    for i in range(n-2,-1,-1):
        temp[1][i]=arr[1][i+1]
    temp[0][0]=arr[1][0]
    arr=copy.deepcopy(temp)'''

    temp=[0]*n
    for i in range(n):
        if i==n-1:
            robot[0]=0
            continue
        if robot[i]==1:
            temp[i+1]=1
    robot=copy.deepcopy(temp)

    #2
    for i in range(n-1,-1,-1):
        if robot[i]==0:
            continue
        if i==n-1:
            robot[i]=0
            continue
        if arr[0][i+1]>=1 and robot[i+1]==0:
            robot[i+1]=1
            robot[i]=0
            arr[0][i+1]-=1

    #3
    if arr[0][0]!=0:
        arr[0][0]-=1
        robot[0]=1

    #4
    c=0
    c+=arr[0].count(0)
    c+=arr[1].count(0)
    if c>=k:
        break
print(answer)