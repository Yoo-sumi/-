import heapq
def solution(scoville, K):
    answer = 0
    q=[]
    for i in scoville:
        heapq.heappush(q,i)
    while True:
        first=heapq.heappop(q)
        if first>=K:
            break
        if not q:
            return -1
        second=heapq.heappop(q)
        heapq.heappush(q,first+(second*2))
        answer+=1
    return answer
print(solution([12,10,9,3,2,1],7))
#print(solution([1, 2, 3, 9, 10, 12],7))
'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''