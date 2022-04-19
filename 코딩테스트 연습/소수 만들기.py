from itertools import permutations
def solution(nums):
    answer = 0
    li=list(permutations(nums,3))
    arr=[]
    for i in li:
        i=list(i)
        i.sort()
        if i in arr:
            continue
        n=sum(i)
        flag=True
        for j in range(2,n):
            if n%j==0:
                flag=False
                break
        if flag==True:
            answer+=1
            arr.append(i)

    return answer