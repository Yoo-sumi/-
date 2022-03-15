def solution(phone_book):
    answer = True
    dic={}

    for i in phone_book:
        dic[i]=1

    for phone_number in phone_book:
        s=""
        for number in phone_number:
            s+=number
            if s in dic and s !=phone_number:
                answer=False
                return answer
    return answer

print(solution(["12","123","1235","567","88"]))

'''
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''