import copy
def solution():
    n,m,r=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    oper=list(map(int,input().split()))
    for o in oper:
        temp=[]
        if o==1:
            for i in range(n-1,-1,-1):
                temp.append(arr[i])
        elif o==2:
            temp=[[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m-1,-1,-1):
                    temp[i][m-1-j]=arr[i][j]
        elif o==3:
            temp=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n-1,-1,-1):
                    temp[i][n-1-j]=arr[j][i]
            n,m=m,n
        elif o==4:
            temp=[[0]*n for _ in range(m)]
            for i in range(m-1,-1,-1):
                for j in range(n):
                    temp[m-1-i][j]=arr[j][i]
            n,m=m,n
        elif o==5:
            temp=[[0]*m for _ in range(n)]
            x,y=0,0
            start_n,mid_n,end_n=0,n//2,n
            start_m,mid_m,end_m=0,m//2,m
            group=[(start_n,mid_n,start_m,mid_m),(start_n,mid_n,mid_m,end_m),(mid_n,end_n,start_m,mid_m),(mid_n,end_n,mid_m,end_m)]
            clock=[2,0,3,1]
            for c in clock:
                a,b,c,d=group[c]
                for i in range(a,b):
                    for j in range(c,d):
                        if x==n//2-1 and y==m//2:
                            x=0
                            y=m//2
                        elif x==n//2-1 and y==m:
                            x=n//2
                            y=0
                        elif x==n-1 and y==m//2:
                            x=n//2
                            y=m//2
                        elif y==m//2:
                            y=0
                            x+=1
                        elif y==m:
                            y=m//2
                            x+=1
                        temp[x][y]=arr[i][j]
                        y+=1
        elif o==6:
            temp=[[0]*m for _ in range(n)]
            x,y=0,0
            start_n,mid_n,end_n=0,n//2,n
            start_m,mid_m,end_m=0,m//2,m
            group=[(start_n,mid_n,start_m,mid_m),(start_n,mid_n,mid_m,end_m),(mid_n,end_n,start_m,mid_m),(mid_n,end_n,mid_m,end_m)]
            clock=[1,3,0,2]
            for c in clock:
                a,b,c,d=group[c]
                for i in range(a,b):
                    for j in range(c,d):
                        if x==n//2-1 and y==m//2:
                            x=0
                            y=m//2
                        elif x==n//2-1 and y==m:
                            x=n//2
                            y=0
                        elif x==n-1 and y==m//2:
                            x=n//2
                            y=m//2
                        elif y==m//2:
                            y=0
                            x+=1
                        elif y==m:
                            y=m//2
                            x+=1
                        temp[x][y]=arr[i][j]
                        y+=1
        arr=copy.deepcopy(temp)
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print()
solution()