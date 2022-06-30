def R(arr):
    r=[[] for _ in range(len(arr))]
    width=0
    for i in range(len(arr)):
        temp=[]
        li=set(arr[i])
        for j in li:
            if j==0:
                continue
            temp.append((j,arr[i].count(j)))
        temp.sort(key=lambda x:(x[1],x[0]))
        for a,b in temp:
            if len(r[i])==100:
                break
            r[i]+=[a]
            if len(r[i])==100:
                break
            r[i]+=[b]
        width=max(width,len(r[i]))
    for i in range(len(r)):
        if len(r[i])!=width:
            r[i]+=[0]*(width-len(r[i]))
    return r
def C(arr):
    r=[[] for _ in range(len(arr[0]))]
    width=0
    for i in range(len(arr[0])):
        dic={}
        temp=[]
        for j in range(len(arr)):
            dic[arr[j][i]]=dic.get(arr[j][i],0)+1
        for j in dic.keys():
            if j==0:
                continue
            temp.append((j,dic[j]))
        temp.sort(key=lambda x:(x[1],x[0]))
        for a,b in temp:
            if len(r[i])==100:
                break
            r[i]+=[a]
            if len(r[i])==100:
                break
            r[i]+=[b]
        width=max(width,len(r[i]))
    for i in range(len(r)):
        if len(r[i])!=width:
            r[i]+=[0]*(width-len(r[i]))
    width,height=len(r[0]),len(r)
    c=[[0]*height for _ in range(width)]
    for i in range(width):
        for j in range(height):
            c[i][j]=r[j][i]
    return c
def solution():
    r,c,k=map(int,input().split())
    arr=[]
    for _ in range(3):
        arr.append(list(map(int,input().split())))
    stack=[]
    stack.append((arr,0))
    while stack:
        now_arr,count=stack.pop(0)
        if count>100:
            return -1
        if 0<=r-1<len(now_arr) and 0<=c-1<len(now_arr[0]):
            if now_arr[r-1][c-1]==k:
                return count
        if len(now_arr[0])<=len(now_arr):
            stack.append((R(now_arr),count+1))
        if len(now_arr[0])>len(now_arr):
            stack.append((C(now_arr),count+1))
    return -1

print(solution())
