n=5
arr=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
#left->down->right->up
x,y=n//2,n//2
dx=[0,1,0,-1]
dy=[-1,0,1,0]
d=2
cnt=1
f=True
while f:
    for _ in range(2):
        for _ in range(cnt):
            x+=dx[d]
            y+=dy[d]
            if (x,y)==(0,0):
                f=False
                break
        if not f:
            break
        d=(d-1)%4
    cnt+=1

def clock_rotate():
    global arr
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=arr[n-1-j][i]
    for i in temp:
        for j in i:
            print(j,end=" ")
        print()
def rclock_rotate():
    global arr
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=arr[j][n-1-i]
    for i in temp:
        for j in i:
            print(j,end=" ")
        print()
def rclock_rotate180():
    global arr
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=arr[n-1-i][n-1-j]
    for i in temp:
        for j in i:
            print(j,end=" ")
        print()
def rever_lr():
    global arr
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=arr[i][n-1-j]
    for i in temp:
        for j in i:
            print(j,end=" ")
        print()
    return temp
def rever_ud():
    global arr
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=arr[n-1-i][j]
    for i in temp:
        for j in i:
            print(j,end=" ")
        print()
    return temp
arr=rever_lr()
print()
arr=rever_ud()
print()
for i in arr:
    for j in i:
        print(j,end=" ")
    print()