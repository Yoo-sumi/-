def solution(n,m,r,arr):
    nn,mm=n,m
    for _ in range(r):
        x,y,n,m=0,0,nn,mm
        i=0
        while True:
            if n<=1 or m<=1:
                break
            temp=arr[x][y]
            #맨 왼쪽
            for i in range(x+1,x+n):
                arr[i][y],temp=temp,arr[i][y]
            x=i
            #맨 아래쪽
            for i in range(y+1,y+m):
                arr[x][i],temp=temp,arr[x][i]
            y=i
            #맨 오른쪽
            for i in range(x-1,x-n,-1):
                arr[i][y],temp=temp,arr[i][y]
            x=i
            #맨 왼쪽
            for i in range(y-1,y-m,-1):
                arr[x][i],temp=temp,arr[x][i]
            y=i
            x,y,n,m=x+1,y+1,n-2,m-2
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()


n,m,r=map(int,input().split()) #세로, 가로, 회전 수
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

solution(n,m,r,arr)
