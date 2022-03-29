def solution(phone_book):
    answer=True
    dic={}
    for i in phone_book:
        dic[i]=1
    for i in phone_book:
        s=""
        for j in i:
            s+=j
            if dic.get(s,-1)==1 and s!=i:
                answer=False
                break
    return answer

print(solution(["119", "97674223", "119524421"]))