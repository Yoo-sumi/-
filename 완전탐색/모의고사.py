def solution(answers):
    array=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    result=[]
    for j in range(3):
        count=0
        index=0
        for i in answers:
            if i==array[j][index%len(array[j])]:
                count+=1
            index+=1
        answer.append((count,j+1))
    answer.sort(key=lambda x:(-x[0],x[1]))
    for i in answer:
        if answer[0][0]==i[0]:
            result.append(i[1])
    result.sort()
    return result

print(solution([1,3,2,4,2]))

'''
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''

'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
'''