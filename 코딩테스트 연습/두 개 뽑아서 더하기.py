import datetime
from itertools import combinations
def solution(numbers):
    answer = []
    li=list(set(combinations(numbers,2)))
    for a,b in li:
        if not a+b in answer:
            answer.append(a+b)
    answer.sort()
    return answer
datetime.timedelta()