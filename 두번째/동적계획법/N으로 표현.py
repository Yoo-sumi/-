def solution(N, number):
    n=1
    array=[[] for _ in range(9)]
    while True:
        if n>8:
            return -1
            break
        array[n].append(int(str(N)*n))
        for i in range(1,(n//2)+1):
            for j in array[i]:
                for h in array[n-i]:
                    array[n].append(j+h)
                    array[n].append(j-h)
                    array[n].append(h-j)
                    array[n].append(j*h)
                    if j!=0:
                        array[n].append(h//j)
                    elif h!=0:
                        array[n].append(j//h)
        if number in array[n]:
            return n
        n+=1
print(solution(2,11))
'''
N	number	return
5	12	4
2	11	3
'''