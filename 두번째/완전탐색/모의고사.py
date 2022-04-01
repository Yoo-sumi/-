def solution(answers):
    answer = []
    result=[]
    data=[[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(data)):
        count=0
        for j in range(len(answers)):
            if answers[j]==data[i][j%len(data[i])]:
                count+=1
        answer.append((count,i))
    answer.sort(key=lambda x:(-x[0],x[1]))

    m=answer[0][0]
    for a,b in answer:
        if m>a:
            break
        result.append(b+1)
    result.sort()
    return result
print(solution([1,3,2,4,2]))
'''
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''