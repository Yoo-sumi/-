import heapq
def solution(jobs):
    length=len(jobs)
    time=0
    result=0
    q=[]
    jobs.sort(reverse=True)
    while True:
        if not q and not jobs:
            break
        count=0
        for i in jobs[::-1]:
            if i[0]>time:
                break
            heapq.heappush(q,(i[1],i[0]))
            count+=1
        if count==0 and len(q)==0:
            time+=1
            continue
        for i in range(count):
            jobs.pop()
        now=heapq.heappop(q)
        result+=now[0]+(time-now[1])
        time+=now[0]
    return result//length
print(solution([[0, 3], [1, 9], [2, 6]]))
'''
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
'''