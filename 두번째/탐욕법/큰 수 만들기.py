def solution(number, k):
    q=[]
    q.append(number[0])
    for i in range(1,len(number)):
        if k==0 :
            q+=number[i:len(number)]
            break
        if q[-1]<number[i]:
            while q:
                if q[-1]>=number[i] or k==0:
                    break
                q.pop()
                k-=1
        q.append(number[i])
    if k!=0:
        answer="".join(q[:-k])
    else:
        answer="".join(q)
    return answer
print(solution("4177252841",4))
'''
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''