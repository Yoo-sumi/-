import itertools
def solution(numbers):
    answer = 0
    numbers=list(numbers)
    result=[]
    array=[]
    for h in range(len(numbers)):
        array+=list(itertools.permutations(numbers,h+1))
    for i in array:
        s=int("".join(i))
        if not s in result:
            result.append(s)
    for i in result:
        j=0
        if 0<=i<=1:
            continue
        for j in range(2,i+1):
            if i%j==0:
                break
        if j==i:
            answer+=1
    return answer
print(solution("17"))
'''
numbers	return
"17"	3
"011"	2'''