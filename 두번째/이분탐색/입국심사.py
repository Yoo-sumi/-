def solution(n, times):
    answer = 0
    left=0
    right=n*max(times)
    while left<=right:
        mid=(left+right)//2
        count=0
        for i in times:
            count+=mid//i
            if count>=n:
                break
        if count>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return answer
print(solution(6,[7,10]))
'''
n	times	return
6	[7, 10]	28
'''