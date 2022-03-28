def solution(participant, completion):
    answer = ''
    data={}
    for i in participant:
        data[i]=data.get(i,0)+1
    for i in completion:
        data[i]=data.get(i,0)-1
    for i in data.keys():
        if data[i]==1:
            answer = i
            break
    return answer
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
'''
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
'''