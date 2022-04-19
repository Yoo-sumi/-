def solution(lottos, win_nums):
    answer = []
    score=1
    for i in range(6):
        if not win_nums[i] in lottos:
            score+=1
    m=score-lottos.count(0)
    n=score
    if m>=6:
        m=6
    if n>=6:
        n=6
    return [m,n]