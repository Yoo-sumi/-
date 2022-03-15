def solution(participant, completion):
    '''participant.sort()
    completion.sort()
    print(participant)
    answer=""

    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            answer=participant[i]
            return answer
    return participant[:-1]'''


    hashDict = {}
    sumHash = 0 # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        print(hash(part))
        hashDict[hash(part)] = part
        sumHash += hash(part)
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
# ["leo", "kiki", "eden"], ["eden", "kiki"]
# ["mislav", "stanko", "mislav", "ana"]
# ["stanko", "ana", "mislav"]