import heapq

def solution(operations):
    answer = []
    min_heap=[]
    max_heap=[]

    for i in operations:
        a=i[0]
        b=int(i[2:])
        if a=="I":
            heapq.heappush(min_heap, b)
            heapq.heappush(max_heap, -b)
        else:
            if not min_heap:
                continue
            if b<0:
                heapq.heappop(min_heap)
                max_heap.pop()
            else:
                heapq.heappop(max_heap)
                min_heap.pop()
        print(min_heap)
    if not min_heap:
        return [0,0]
    else:
        return [-max_heap[0],min_heap[0]]
print(solution(["I 16","I 16","D 1"]))
'''
operations	return
["I 16","D 1"]	[0,0]
["I 7","I 5","I -5","D -1"]	[7,5]
'''