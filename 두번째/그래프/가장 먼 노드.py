def solution(n, edge):
    q=[]
    route=[n]*(n+1)
    array=[[] for _ in range(n+1)]
    for a,b in edge:
        array[a].append(b)
        array[b].append(a)
    q.append((1,0))
    while q:
        add=[]
        while q:
            now=q.pop()
            route[now[0]]=min(route[now[0]],now[1])
            for i in array[now[0]]:
                add.append((i,now[1]+1))
            array[now[0]]=[]
        for i in add:
            q.append(i)
    mm=max(route[1:])
    return route.count(mm)
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))
'''
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
'''