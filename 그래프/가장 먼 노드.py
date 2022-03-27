from collections import deque
def solution(n, edge):
    flag=[False]*(n+1)
    distance=[n+1]*(n+1)
    q=deque()
    data=[[] for _ in range(n+1)]
    for a,b in edge:
        data[a].append(b)
        data[b].append(a)
    q.append((1,0))
    flag[1]=True
    while q:
        now=q.popleft()
        distance[now[0]]=min(distance[now[0]],now[1]+1)
        for i in data[now[0]]:
            if flag[i]==False:
                q.append((i,now[1]+1))
                flag[i]=True
    val=max(distance[1:])
    return distance.count(val)
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
'''
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
'''