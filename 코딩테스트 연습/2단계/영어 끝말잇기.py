def solution(n, words):
    answer = []
    flag=False
    if len(words[0])==1:
        return [0,0]
    for i in range(1,len(words)):
        if len(words[i])==1:
            flag=True
            break
        if words[i] in words[:i]:
            flag=True
            break
        if words[i-1][-1]!=words[i][0]:
            flag=True
            break
    if flag:
        if i%n==0:
            answer=[1,i//n+1]
        else:
            answer=[i%n+1,i//n+1]
    else:
        answer=[0,0]
    return answer