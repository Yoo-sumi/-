def solution(x, n):
    answer = []
    plus=x
    while True:
        if len(answer)==n:
            break
        answer.append(x)
        x+=plus
    return answer