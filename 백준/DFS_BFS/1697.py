import sys
from collections import deque

input=sys.stdin.readline
n,k=map(int,input().split())
q=deque()
visited=[0 for _ in range(100001)]
def solution(n,k):
    q.append(n)
    count=0
    while q:
        a=[]
        flag=False
        while q:
            now=q.popleft()
            visited[now]=1
            if now==k:
                flag=True
                break
            if 0<=now-1<=100000:
                if visited[now-1]==0:
                    a.append(now-1)
            if 0<=now+1<=100000:
                if visited[now+1]==0:
                    a.append(now+1)
            if 0<=now*2<=100000:
                if visited[now*2]==0:
                    a.append(now*2)
        if flag==True:
            break
        for i in a:
            q.append(i)
        count+=1
    return count
print(solution(n,k))