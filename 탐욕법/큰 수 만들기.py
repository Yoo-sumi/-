def solution(number, k):
    stack=[]
    stack.append(number[0])

    for i in range(1,len(number)):
        if k==0:
            for j in range(i,len(number)):
                stack.append(number[j])
            break
        if stack[-1]<number[i]:
            while stack :
                if stack[-1]>=number[i] or k==0:
                    break
                stack.pop()
                k-=1

        stack.append(number[i])
    if k!=0:
        answer="".join(stack[:-k])
    else:
        answer="".join(stack)
    return answer
'''
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

print(solution("989999999999999999999999999999999999999999999999999999999999999999999",68))
#989999999999999999999999999999999999999999999999999999999999999999999