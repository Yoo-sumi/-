import heapq
def solution(N, road, K):
    result=[int(1e9)]*(N+1)
    array=[[] for _ in range(N+1)]
    q=[]
    heapq.heappush(q,(0,1))
    for a,b,c in road:
        array[a].append((b,c))
        array[b].append((a,c))
    result[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if result[now]<dist:
            continue
        for a,b in array[now]:
            if result[a]>dist+b:
                result[a]=dist+b
                heapq.heappush(q,(result[a],a))
    result=sorted(result[1:])
    count=0
    for i in result:
        if i>K:
            break
        count+=1
    return count