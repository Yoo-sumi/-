def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(4):
            mm=-1
            index=-1
            for h in range(4):
                if h==j:
                    continue
                if mm<land[i-1][h]:
                    index=h
                mm=max(mm,land[i-1][h])
            land[i][j]+=mm
    return max(land[len(land)-1])