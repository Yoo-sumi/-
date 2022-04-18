from collections import deque
def get_score(array1,array2):
    sum1=0
    sum2=0
    for i in range(11):
        if not (array1[i]==array2[i]==0):
            if array1[i]<array2[i]:
                sum2+=10-i
            else:
                sum1+=10-i
    return sum1,sum2
def solution(n, info):
    answer = []
    peach=[]
    q=deque()
    q.append((0,[0]*11))
    for i in info:
        peach.append(i)
    maxGap=0
    while q:
        index,lion=q.popleft()
        if sum(lion)==n:
            p,l=get_score(peach,lion)
            if p<l:
                gap=l-p
                if maxGap>gap:
                    continue
                if maxGap<gap:
                    maxGap=gap
                    answer.clear()
                answer.append(lion)
        elif index==10:
            tmp=lion.copy()
            tmp[index]=n-sum(tmp)
            q.append((-1,tmp))
        elif sum(lion)>n:
            continue
        else:
            tmp = lion.copy()
            tmp[index] = peach[index]+1
            q.append((index+1, tmp))
            tmp2 = lion.copy()
            tmp2[index] = 0
            q.append((index+1, tmp2))

    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))