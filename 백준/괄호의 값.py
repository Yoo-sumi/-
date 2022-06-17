def solution(s):
    stack=[]
    if s[0]==')' or s[0]==']' or len(s)%2!=0:
        return 0
    stack.append(s[0])
    for i in s[1:]:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            temp=-1
            if not stack:
                return 0
            if type(stack[-1])==int:
                temp=stack.pop()
            if not stack:
                return 0
            if stack[-1]=='(':
                stack.pop()
                if temp!=-1:
                    if stack:
                        if type(stack[-1])==int:
                            stack.append(stack.pop()+(temp*2))
                            continue
                    stack.append(temp*2)
                else:
                    if stack:
                        if type(stack[-1])==int:
                            stack.append(stack.pop()+(2))
                            continue
                    stack.append(2)
                continue
            else:
                return 0
            stack.append(i)
        elif i==']':
            temp=-1
            if not stack:
                return 0
            if type(stack[-1])==int:
                temp=stack.pop()
            if not stack:
                return 0
            if stack[-1]=='[':
                stack.pop()
                if temp!=-1:
                    if stack:
                        if type(stack[-1])==int:
                            stack.append(stack.pop()+(temp*3))
                            continue
                    stack.append(temp*3)
                else:
                    if stack:
                        if type(stack[-1])==int:
                            stack.append(stack.pop()+(3))
                            continue
                    stack.append(3)
                continue
            else:
                return 0
            stack.append(i)
    if type(stack[0])==int and len(stack)==1:
        return stack[0]
    else:
        return 0
print(solution(str(input())))