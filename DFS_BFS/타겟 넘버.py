def solution(numbers, target):
    def dfs(index,sum):
        if sum==target and index==len(numbers)-1:
            return 1
        if index+1>=len(numbers):
            return 0
        a=dfs(index+1,sum+numbers[index+1])
        b=dfs(index+1,sum-numbers[index+1])

        return a+b
    a=dfs(0,numbers[0])
    b=dfs(0,-numbers[0])
    answer = a+b

    return answer
print(solution([1, 1, 1, 1, 1],3))
'''
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
'''