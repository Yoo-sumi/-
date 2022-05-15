from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q=deque()
    if cacheSize==0:
        return 5*len(cities)
    for i in cities:
        i=i.lower()
        if i in q:
            answer+=1
            q.remove(i)
            q.append(i)
        else:
            answer+=5
            if len(q)==cacheSize:
                q.popleft()
            q.append(i)
    return answer