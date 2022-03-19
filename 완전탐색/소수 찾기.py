import itertools
def solution(numbers):
    array=list(numbers)
    result=[]
    permut=[]
    for i in range(len(array)):
        permut+=list(itertools.permutations(array,i+1))
    for i in permut:
        if not int("".join(i)) in result:
            result.append(int("".join(i)))
    count=len(result)
    for i in result:
        if i<=1:
            count-=1
        for j in range(2,i):
            if i%j==0:
                count-=1
                break
    return count
print(solution("011"))
'''
numbers	return
"17"	3
"011"	2
'''