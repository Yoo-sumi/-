def solution(citations):
    citations.sort()
    n=h=len(citations)
    while True:
        index=n
        for i in range(len(citations)):
            if h<=citations[i]:
                index=i
                break
        array=citations[:index]
        if h<=n-index:
            if not array:
                break
            if array[-1]<=h:
                break
        h-=1
        if h==0:
            break
    return h

print(solution([0,1,2]))
'''
citations	return
[3, 0, 6, 1, 5]	3
'''