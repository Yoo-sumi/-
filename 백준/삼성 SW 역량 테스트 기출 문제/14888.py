from collections import deque
import copy
n=int(input())
array=list(map(int,input().split()))
operation=list(map(int,input().split()))
q=deque()
q.append((array[0],operation))
def excute(v,i,size):
    result=0
    if i==0:
        result=v+array[n-size]
    elif i==1:
        result=v-array[n-size]
    elif i==2:
        result=v*array[n-size]
    elif i==3:
        if v<0:
            result=-v//array[n-size]
            result=-result
        else:
            result=v//array[n-size]
    return result
min_value=int(1e9)
max_value=-int(1e9)
while q:
    v,oper=q.popleft()
    if sum(oper)==0:
        min_value=min(min_value,v)
        max_value=max(max_value,v)
        continue

    for i in range(4):
        temp=copy.deepcopy(oper)
        if oper[i]>0:
            temp[i]-=1
            re=excute(v,i,sum(oper))
            q.append((re,temp))
print(max_value)
print(min_value)