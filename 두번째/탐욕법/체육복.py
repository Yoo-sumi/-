def solution(n, lost, reserve):
    array=[1]*n
    for i in lost:
        array[i-1]-=1
    for i in reserve:
        array[i-1]+=1
    for i in range(n):
        if array[i]==2:
            if i>0:
                if array[i-1]==0:
                    array[i-1]+=1
                    array[i]-=1
                    continue
            if i+1<n:
                if array[i+1]==0:
                    array[i+1]+=1
                    array[i]-=1
                    continue
    return n-array.count(0)

print(solution(5,[2,4],[1,3,5]))
'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''