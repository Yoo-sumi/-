import heapq
def solution(operations):
    q_min=[]
    q_max=[]
    for i in operations:
        if i[0]=="I":
            heapq.heappush(q_min,int(i[2:]))
            heapq.heappush(q_max,-int(i[2:]))
        elif i[0]=="D":
            if not q_min:
                continue
            if int(i[2:])<0:
                heapq.heappop(q_min)
                q_max.pop()
            else:
                heapq.heappop(q_max)
                q_min.pop()
    if not q_min:
        return [0,0]
    return [-q_max[0],q_min[0]]
print(solution(["I 7","I 5","I -5","D 1"]))
'''
operations	return
["I 16","D 1"]	[0,0]
["I 7","I 5","I -5","D -1"]	[7,5]
'''