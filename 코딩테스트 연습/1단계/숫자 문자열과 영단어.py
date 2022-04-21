def solution(s):
    answer = ""
    dic={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
         "eight":8,"nine":9}
    n=""

    for i in s:
        if n in dic.keys():
            answer+=str(dic[n])
            n=""
        if not 48<=ord(i)<=57:
            n+=i
        else:
            answer+=i
            n=""
    if n in dic.keys():
        answer+=str(dic[n])


    return int(answer)