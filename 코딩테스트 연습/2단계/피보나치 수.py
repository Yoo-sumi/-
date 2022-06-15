def solution(n):
    stack=[0,1]
    count=1
    while True:
        if count==n:
            break
        stack.append(sum(stack))
        stack.pop(0)
        count+=1
    return stack[-1]%1234567