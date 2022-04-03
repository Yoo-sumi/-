def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left=0
    right=len(people)-1
    while left<=right:
        if people[left]+people[right]<=limit:
            right-=1
        left+=1
        answer+=1
    return answer
print(solution([70, 50,80, 50],100))
'''
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
'''