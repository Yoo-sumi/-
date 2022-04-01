def solution(brown, yellow):
    answer = []
    array=[]
    for i in range(1,yellow+1):
        if yellow%i==0 and i>=yellow//i:
            array.append((i,yellow//i))
    print(array)
    for a,b in array:
        if (a+2)*(b+2)-yellow==brown:
            answer=[(a+2),(b+2)]
            break
    return answer
print(solution(24,24))
'''
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''