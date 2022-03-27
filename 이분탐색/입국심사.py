def solution(n, times):
    answer=0
    times.sort()
    start=min(times)
    end=max(times)*n
    while start<=end:
        mid=(start+end)//2
        count=0
        for i in times:
            count+=mid//i
        if count>=n:
            answer=mid # 최단시간을 구해야 하기 때문에, 여기에서 result 기록
            end=mid-1
        else:
            start=mid+1
    return answer

print(solution(6,[7,10]))
'''
n	times	return
6	[7, 10]	28
'''