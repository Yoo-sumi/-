def solution(N, number):
    array=[0,[N]]
    if N==number:
        return 1
    for i in range(2,9):
        temp=[]

        temp.append(int(str(N)*i))
        for h in range(1,len(array)//+1):
            for x in array[h]:
                for y in array[i-h]:
                    temp.append(x*y)
                    temp.append(x+y)
                    temp.append(x-y)
                    temp.append(y-x)
                if x!=0:
                    temp.append(y//x)
                if y!=0:
                    temp.append(x//y)
        if number in temp:
            return i
        array.append(temp)
    return -1
print(solution(8,53))
'''
N	number	return
5	12	4
2	11	3
8보다 크면 -1 return'''