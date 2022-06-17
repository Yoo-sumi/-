from collections import deque
n,m=map(int,input().split())
array=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
flag=[]
r=(0,0)
b=(0,0)
for j in range(n):
    li=list(str(input()))
    for i in range(m):
        if li[i]=='R':
            r=(j,i)
        elif li[i]=='B':
            b=(j,i)
    array.append(li)
flag.append((r,b))
array[r[0]][r[1]]='.'
array[b[0]][b[1]]='.'
def bfs():
    q=deque()
    q.append((r,b,0))
    while q:
        temp=[]
        while q:
            rnow,bnow,count=q.popleft()
            if count>10:
                continue
            if array[bnow[0]][bnow[1]]=='O':
                continue
            if array[rnow[0]][rnow[1]]=='O':
                return count
            for i in range(4):
                rx,ry=rnow[0],rnow[1]
                bx,by=bnow[0],bnow[1]
                rflag,bflag=False,False
                while True:
                    if rflag and bflag:
                        break
                    if not rflag:
                        rx+=dx[i]
                        ry+=dy[i]
                        if array[rx][ry]=='O':
                            rflag=True
                        if array[rx][ry]=='#':
                            rx-=dx[i]
                            ry-=dy[i]
                            rflag=True
                    if not bflag:
                        bx+=dx[i]
                        by+=dy[i]
                        if array[bx][by]=='O':
                            bflag=True
                        if array[bx][by]=='#':
                            bx-=dx[i]
                            by-=dy[i]
                            bflag=True
                    if (rx,ry)==(bx,by):
                        if rflag and not bflag:
                            bx-=dx[i]
                            by-=dy[i]
                            bflag=True
                        elif not rflag and bflag:
                            rx-=dx[i]
                            ry-=dy[i]
                            rflag=True
                if not ((rx,ry),(bx,by)) in flag:
                    temp.append(((rx,ry),(bx,by),count+1))
                    flag.append(((rx,ry),(bx,by)))
        for aa,bb,cc in temp:
            q.append((aa,bb,cc))
    return -1
print(bfs())
