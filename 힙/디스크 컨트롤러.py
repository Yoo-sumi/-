import heapq

def solution(jobs):
    answer = 0
    length=len(jobs)
    q=[]
    jobs.sort(reverse=True)
    value=jobs.pop()
    heapq.heappush(q,(value[1],value[0]))
    time=value[0]
    while q or jobs:
        if len(q)==0:
            time+=1
        else:
            now=heapq.heappop(q)
            time+=now[0]
            answer+=(time-now[1])
        while jobs:
            if jobs[-1][0]<=time:
                value=jobs.pop()
                heapq.heappush(q,(value[1],value[0]))
            else:
                break
    return answer//length
print(solution([[0, 3], [1, 9], [30, 6]]))
'''
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
'''