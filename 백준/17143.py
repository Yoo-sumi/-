import sys,copy
input=sys.stdin.readline
def solution():
    R,C,M=map(int,input().split())
    graph=[[() for _ in range(C)] for _ in range(R)]
    shark={}
    if M==0:
        return 0
    for _ in range(M):
        r,c,s,d,z=map(int,input().split())
        r-=1
        c-=1
        graph[r][c]=(s,d,z)
        shark[(r,c)]=1

    king=-1
    answer=0
    while True:
        #1
        king+=1
        if king==C:
            break
        #2
        for i in range(0,R):
            if graph[i][king]:
                answer+=graph[i][king][2]
                graph[i][king]=0
                del shark[(i,king)]
                break
        temp=[[() for _ in range(C)] for _ in range(R)]
        #3
        li=list(shark.keys())
        dic={}
        for x,y in li:
            start_x,start_y=-1,-1
            dis,size=graph[x][y][1],graph[x][y][0]
            #up_down
            if 1<=dis<=2:
                start_x=x
                for _ in range(size):
                    if start_x==R:
                        start_x-=2
                        dis=1
                    elif start_x==-1:
                        start_x+=2
                        dis=2
                    if dis==1:
                        start_x-=1
                    elif dis==2:
                        start_x+=1
                if start_x==R:
                    start_x-=2
                    dis=1
                elif start_x==-1:
                    start_x+=2
                    dis=2
            #left_right
            elif 3<=dis<=4:
                start_y=y
                for _ in range(size):
                    if start_y==C:
                        start_y-=2
                        dis=4
                    elif start_y==-1:
                        start_y+=2
                        dis=3
                    if dis==3:
                        start_y+=1
                    elif dis==4:
                        start_y-=1
                if start_y==C:
                    start_y-=2
                    dis=4
                elif start_y==-1:
                    start_y+=2
                    dis=3
            if start_x==-1:
                if temp[x][start_y]:
                    if temp[x][start_y][2]<graph[x][y][2]:
                        temp[x][start_y]=(size,dis,graph[x][y][2])
                        dic[(x,start_y)]=1
                else:
                    temp[x][start_y]=(size,dis,graph[x][y][2])
                    dic[(x,start_y)]=1
            elif start_y==-1:
                if temp[start_x][y]:
                    if temp[start_x][y][2]<graph[x][y][2]:
                        temp[start_x][y]=(size,dis,graph[x][y][2])
                        dic[(start_x,y)]=1
                else:
                    temp[start_x][y]=(size,dis,graph[x][y][2])
                    dic[(start_x,y)]=1
        shark=dic
        graph=copy.deepcopy(temp)
    return answer
print(solution())