def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
            continue
        if answer[-1]==i:
            continue
        answer.append(i)
    return answer