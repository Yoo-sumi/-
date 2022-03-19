def solution(citations):
    citations.sort()
    index=len(citations)
    while True:
        for i in range(len(citations)):
            if index<=citations[i]:
                if len(citations)-i>=index:
                    return index
                break
        index-=1

print(solution([3, 6, 1, 5,10]))
'''
citations	return
[3, 0, 6, 1, 5]	3
'''