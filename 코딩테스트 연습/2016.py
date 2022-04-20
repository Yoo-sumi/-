import datetime
def solution(a, b):
    answer = ''
    dic={0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
    d=datetime.datetime(2016,a,b)
    answer=dic[d.weekday()]
    return answer