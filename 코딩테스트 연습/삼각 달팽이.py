def solution(n):
    array=[[0]*n for _ in range(n)]
    plus=[i for i in range(n,0,-1)]
    plus[0]-=1
    x,y=0,0
    num=1
    index=0
    rotate=1
    while True:
        array[x][y]=num
        if num==rotate+plus[index]:
            index+=1
            if index>=len(plus):
                break
            rotate=num
        num+=1
        if index%3==0:
            x+=1
        elif index%3==1:
            y+=1
        elif index%3==2:
            x-=1
            y-=1
    result=[]
    for i in array:
        for j in i:
            if j==0:
                break
            result.append(j)

    return result