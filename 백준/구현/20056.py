n,m,k=map(int,input().split())
fireball={}
for _ in range(m):
    li=list(map(int,input().split()))
    fireball[(li[0],li[1])]=fireball.get((li[0],li[1]),[])+[li[2:]]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
for _ in range(k):
    #move
    li=fireball.keys()
    temp={}
    for x,y in li:
        ball=fireball[(x,y)]
        for m,s,d in ball:
            nx=(x+dx[d]*s)%n
            ny=(y+dy[d]*s)%n
            temp[(nx,ny)]=temp.get((nx,ny),[])+[[m,s,d]]
    li=temp.keys()
    for x,y in li:
        nm,ns,nd=0,0,[]
        ball=temp[(x,y)]
        if len(ball)<2:
            continue
        odd,even=True,True
        for m,s,d in ball:
            nm+=m
            ns+=s
            if d%2==0:
                odd=False
            if d%2!=0:
                even=False
        nm,ns=nm//5,ns//len(ball)
        if odd or even:
            nd=[0,2,4,6]
        else:
            nd=[1,3,5,7]
        temp2=[]
        for i in range(4):
            if nm==0:
                continue
            temp2.append([nm,ns,nd[i]])
        temp[(x,y)]=temp2
    fireball=temp
answer=0
for ball in fireball.values():
    for m,s,d in ball:
        answer+=m
print(answer)

