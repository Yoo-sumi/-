import heapq
def solution(scoville, K):
    answer = 0
    q=[]
    for i in scoville:
        heapq.heappush(q,i)
    while True:
        print(q)
        if q[0]>=K:
            break
        if len(q)==1:
            return -1

        first=heapq.heappop(q)
        second=heapq.heappop(q)
        new=first+(second*2)
        heapq.heappush(q,new)
        answer+=1
    return answer
print(solution([1, 2, 3, 9, 10, 12]	,1000))
'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''