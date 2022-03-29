def solution(clothes):
    answer = 1
    dic={}
    for a,b in clothes:
        dic[b]=dic.get(b,0)+1
    for i in dic.keys():
        answer*=(dic[i]+1)
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))