from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    arr=[]
    li=list(permutations(['-','+','*'],3))
    array=[]
    s=""
    for i in expression:
        if i in ['-','+','*']:
            arr.append(s)
            arr.append(i)
            s=""
        else:
            s+=i
    arr.append(s)
    q=deque()

    for j in li:
        array=arr.copy()
        for n in range(3):
            for i in array:
                if q:
                    if q[-1]==j[n]:
                        x=q.pop()
                        a=q.pop()
                        if x=="*":
                            q.append(str(int(a)*int(i)))
                        elif x=="+":
                            q.append(str(int(a)+int(i)))
                        elif x=="-":
                            q.append(str(int(a)-int(i)))
                        continue
                q.append(i)
            array=list(q)
            q=deque()
        answer=max(abs(int(array[0])),answer)

    return answer