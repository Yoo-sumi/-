from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer=[]
    for i in course:
        temp=[]
        for order in orders:
            li=list(combinations(sorted(order),i))
            temp+=li
        counters=Counter(temp)
        if len(counters)!=0 and max(counters.values())>=2:
            for counter in counters:
                if counters[counter]==max(counters.values()):
                    answer.append("".join(counter))
    answer.sort()
    return answer