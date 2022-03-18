from collections import deque
def solution(prices):
    answer = []
    qs=deque(prices)
    while qs:
        now=qs.popleft()
        sec=0
        print(qs)
        for q in qs:
            sec+=1
            if now>q:
                break
        answer.append(sec)
    return answer

print(solution([1, 2, 3, 2, 3]))
'''
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''