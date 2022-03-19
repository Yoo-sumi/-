def solution(numbers):
    num=list(map(str,numbers))
    num.sort(key=lambda x: x*3,reverse=True)
    return str(int(''.join(num)))
print(solution([6, 10, 2]))
'''
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''