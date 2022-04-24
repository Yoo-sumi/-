def solution(s):
    n=len(s)
    dic={')':'(','}':'{',']':'['}
    count=0
    for i in range(n):
        words=s[i:n]+s[0:i]
        stack=[]
        flag=True
        for j in range(len(words)):
            if words[j] in [')','}',']']:
                if len(stack)==0:
                    flag=False
                    break
                if stack[-1]!=dic[words[j]]:
                    break
                stack.pop()
            else:
                stack.append(words[j])
        if len(stack)==0 and flag:
            count+=1
    return count