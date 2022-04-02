def solution(numbers, target):
    def dfs(index,value):
        if index==len(numbers):
            if value==target:
                return 1
            return 0
        a=dfs(index+1,value+numbers[index])
        b=dfs(index+1,value-numbers[index])
        return a+b
    answer=dfs(0,0)
    return answer
print(solution([4, 1, 2, 1],4))
'''
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
'''