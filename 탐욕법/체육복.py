def solution(n, lost, reserve):
    array=[1 for _ in range(n)]
    lost.sort()
    reserve.sort()
    for i in lost:
        array[i-1]-=1
    for i in reserve:
        array[i-1]+=1

    for i in lost:
        if i in reserve:
            continue
        if i-2>=0:
            if array[i-2]==2:
                array[i-2]-=1
                array[i-1]+=1
                print(array)
                continue
        if i<n:
            if array[i]==2:
                array[i]-=1
                array[i-1]+=1
                print(array)

    return n-array.count(0)
print(solution(7,[2,3,4],[1,2,3,6]))
'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''