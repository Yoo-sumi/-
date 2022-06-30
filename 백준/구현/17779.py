def divide(n,x,y,d1,d2):
    arr=[[0]*n for _ in range(n)]
    dic={}
    #5
    for i in range(d1+1):
        dic[x+i]=dic.get(x+i,[])+[y-i]
    for i in range(d2+1):
        dic[x+i]=dic.get(x+i,[])+[y+i]
    for i in range(d2+1):
        dic[x+d1+i]=dic.get(x+d1+i,[])+[y-d1+i]
    for i in range(d1+1):
        dic[x+d2+i]=dic.get(x+d2+i,[])+[y+d2-i]
    for i in dic.keys():
        li=dic[i]
        v_min=min(li)
        v_max=max(li)
        for j in range(v_min,v_max+1):
            arr[i][j]=5
    #1
    for i in range(x+d1):
        for j in range(y+1):
            if arr[i][j]==5:
                continue
            arr[i][j]=1
    #2
    for i in range(x+d2+1):
        for j in range(y+1,len(arr)):
            if arr[i][j]==5:
                continue
            arr[i][j]=2
    #3
    for i in range(x+d1,len(arr)):
        for j in range(y-d1+d2):
            if arr[i][j]==5:
                continue
            arr[i][j]=3
    #4
    for i in range(x+d2+1,len(arr)):
        for j in range(y-d1+d2,len(arr)):
            if arr[i][j]==5:
                continue
            arr[i][j]=4
    return arr
def gap(arr,p):
    dic={}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            dic[arr[i][j]]=dic.get(arr[i][j],0)+p[i][j]
    li=list(dic.values())
    return max(li)-min(li)

def solution():
    n=int(input())
    people=[]
    for _ in range(n):
        people.append(list(map(int,input().split())))
    answer=1e9
    for i in range(n):
        for j in range(n):
            for d1 in range(1,n):
                for d2 in range(1,n):
                    if 0<=i<i+d1+d2<n and 0<=j-d1<j<j+d2<n:
                        temp=divide(n,i,j,d1,d2)
                        answer=min(answer,gap(temp,people))
    return answer
print(solution())
