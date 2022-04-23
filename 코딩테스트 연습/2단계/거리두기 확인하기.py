def solution(places):
    answer = []
    dx=[-2,-1,-1,-1,0,0,0,0,1,1,1,2]
    dy=[0,-1,0,1,-2,-1,1,2,-1,0,1,0]
    for i in places:
        array=[[0]*5 for _ in range(5)]
        for j in range(5):
            for h in range(5):
                array[j][h]=i[j][h]
        flag=True
        for i in range(5):
            if flag==False:
                break
            for j in range(5):
                if flag==False:
                    break
                if array[i][j]=='P':
                    for h in range(12):
                        nx=i+dx[h]
                        ny=j+dy[h]
                        if not 0<=nx<5 or not 0<=ny<5:
                            continue
                        if array[nx][ny]=='P':
                            if abs(i-nx)+abs(j-ny)==1:
                                flag=False
                                break
                            if abs(i-nx)+abs(j-ny)==2:
                                if i==nx:
                                    if j<ny:
                                        if array[i][j+1] in ['O','P']:
                                            flag=False
                                            break
                                    elif j>ny:
                                        if array[i][j-1] in ['O','P']:
                                            flag=False
                                            break
                                elif j==ny:
                                    if i<nx:
                                        if array[i+1][j] in ['O','P']:
                                            flag=False
                                            break
                                    elif j>ny:
                                        if array[i-1][j] in ['O','P']:
                                            flag=False
                                            break
                                else:
                                    if array[i][ny] in ['O','P']or array[nx][j] in ['O','P']:
                                        flag=False
                                        break
        if flag==True:
            answer.append(1)
        else:
            answer.append(0)

    return answer