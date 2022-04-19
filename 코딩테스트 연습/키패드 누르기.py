def solution(numbers, hand):
    answer = ''
    dic={1:(0,3), 2:(1,3), 3:(2,3),
         4:(0,2), 5:(1,2), 6:(2,2),
         7:(0,1), 8:(1,1), 9:(2,1),
         '*':(0,0), 0:(1,0), '#':(2,0)}
    left,right=dic['*'],dic['#']
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left=dic[i]
        elif i in [3,6,9]:
            answer+='R'
            right=dic[i]
        else:
            x=dic[i][0]
            y=dic[i][1]

            x1=left[0]
            y1=left[1]

            x2=right[0]
            y2=right[1]

            left_distance=abs(x-x1)+abs(y-y1)
            right_distance=abs(x-x2)+abs(y-y2)

            if left_distance<right_distance:
                answer+='L'
                left=dic[i]
            elif left_distance>right_distance:
                answer+='R'
                right=dic[i]
            else:
                if hand=="right":
                    answer+='R'
                    right=dic[i]
                else:
                    answer+='L'
                    left=dic[i]
    return answer