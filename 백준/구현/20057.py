n=int(input())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))
def sand_move():
    global A
    ddx=[-2,-1,-1,-1,]
#left->down->right->up
x,y=n//2,n//2
dx=[0,1,0,-1]
dy=[-1,0,1,0]
d=0
cnt=1
f=True
while f:
    for _ in range(2):
        for _ in range(cnt):
            print(x,y)
            x+=dx[d]
            y+=dy[d]
            if (x,y)==(0,0):
                f=False
                break
        if not f:
            break
        d=(d+1)%4
    cnt+=1
