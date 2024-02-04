# 50x50 가지 경우의수에다가 총 합도 만들어놔야함

def solution(friends, gifts):
    answers = [0]*len(friends)
    info = [[0]*(len(friends)+1) for _ in range(len(friends)+1)]
    for gift in gifts:
        u,v = gift.split(" ")
        # print(friends.index(u),friends.index(v))
        info[friends.index(u)][friends.index(v)] += 1
    for i in range(len(info)):
        info[i][-1] = sum(info[i])
    for j in range(len(info[0])):
        temp = 0
        for i in range(len(info)):
            temp+=info[i][j]
        info[-1][j] = temp
        
    for i in range(len(info)-1):
        for j in range(len(info[0])-1):
            if info[i][j] > info[j][i]:
                answers[i]+=1
            elif info[i][j] == info[j][i]:
                tempA = info[i][-1]-info[-1][i]
                tempB = info[j][-1]-info[-1][j]
                if tempA>tempB:
                    answers[i]+=1
                elif tempA==tempB:
                    pass
                else:
                    answers[j]+=1
            else:
                answers[j]+=1
    # print(info)
    # print(answers)
    answer = max(answers)//2
    return answer