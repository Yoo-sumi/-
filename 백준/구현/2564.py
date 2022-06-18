def solution():
    answer=0
    #가로, 세로
    m,n=map(int,input().split())
    arr=[]
    me=()
    store=int(input())
    for i in range(store+1):
        d,v=map(int,input().split())
        if d==1:
            if store==i:
                me=(0,0+v)
            else:
                arr.append((0,0+v))
        elif d==2:
            if store==i:
                me=(n,0+v)
            else:
                arr.append((n,0+v))
        elif d==3:
            if store==i:
                me=(0+v,0)
            else:
                arr.append((0+v,0))
        elif d==4:
            if store==i:
                me=(0+v,m)
            else:
                arr.append((0+v,m))
    x1,y1=me
    for x2,y2 in arr:
        if x1==x2==0 or x1==x2==n:
            answer+=abs(y1-y2)
            continue
        if y1==y2==0 or y1==y2==m:
            answer+=abs(x1-x2)
            continue
        if x1==0:
            answer+=min(y1+x2+y2,(m-y1)+x2+(m-y2))
        elif x1==n:
            answer+=min(y1+(n-x2)+y2,(m-y1)+(n-x2)+(m-y2))
        elif y1==0:
            answer+=min(x1+y2+x2,(n-x1)+y2+(n-x2))
        elif y1==m:
            answer+=min(x1+(m-y2)+x2,(n-x1)+(m-y2)+(n-x2))
    return answer

print(solution())
