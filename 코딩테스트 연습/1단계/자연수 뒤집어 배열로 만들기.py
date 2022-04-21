def solution(n):
    answer = []
    n=list(str(n))
    for i in n[::-1]:
        answer.append(int(i))
    return answer