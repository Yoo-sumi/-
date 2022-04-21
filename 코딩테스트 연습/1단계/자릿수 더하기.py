def solution(n):
    answer = 0
    n=str(n)
    for i in list(n):
        answer+=int(i)
    return answer