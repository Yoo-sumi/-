from itertools import permutations
def solution(k, dungeons):
    arr=[i for i in range(len(dungeons))]
    li=list(permutations(arr,len(dungeons)))
    result=-1
    for i in li:
        p=k
        flag=True
        for j in range(len(i)):
            if p<dungeons[i[j]][0]:
                result=max(result,j)
                flag=False
                break
            p-=dungeons[i[j]][1]
        if flag:
            result=max(result,j+1)
    return result