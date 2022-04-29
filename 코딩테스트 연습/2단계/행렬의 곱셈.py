def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr=[]
        for x in range(len(arr2[0])):
            summ=0
            for y in range(len(arr2)):
                summ+=arr1[i][y]*arr2[y][x]
            arr.append(summ)
        answer.append(arr)
    return answer