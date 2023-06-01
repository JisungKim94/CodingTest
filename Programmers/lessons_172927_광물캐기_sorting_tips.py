def solution(picks, minerals):
    answer = 0
    
    Fatigue=[[0]*len(minerals) for i in range(3)]
    newFatigue=[[] for i in range(3)]
    start = 0
    for i,v in enumerate(minerals):
        if v == "diamond":
            Fatigue[0][i] = 1
            Fatigue[1][i] = 5
            Fatigue[2][i] = 25
        if v == "iron":
            Fatigue[0][i] = 1
            Fatigue[1][i] = 1
            Fatigue[2][i] = 5
        if v == "stone":
            Fatigue[0][i] = 1
            Fatigue[1][i] = 1
            Fatigue[2][i] = 1
    
    for i in range(len(minerals)//5):
        i = i*5
        if i+5 > sum(picks)*5:
            continue
        for _ in range(i,i+5,1):
            newFatigue[0].append(sum(Fatigue[0][i:i+5]))
            newFatigue[1].append(sum(Fatigue[1][i:i+5]))
            newFatigue[2].append(sum(Fatigue[2][i:i+5]))
    for _ in range(len(minerals)%5):
        if len(newFatigue[0]) >= sum(picks)*5:
            continue
        newFatigue[0].append(sum(Fatigue[0][-(len(minerals)%5):]))
        newFatigue[1].append(sum(Fatigue[1][-(len(minerals)%5):]))
        newFatigue[2].append(sum(Fatigue[2][-(len(minerals)%5):]))

    # 하고싶은거 : newFatigue[2] 기준으로 정리한 규칙을 [0],[1]에 적용 시키고 싶음..
    # 어캐하는지 모르겠음... 애초에 배열을 [0,1,2][0,1,2] 꼴로 만들면 람다가 되는데 아니면 방법이 없나..?
    # 없는듯.. 그래서 다시 만들거나 zip으로 꼴을 만들어줘야 함
    # newFatigue=sorted(newFatigue,key = lambda x : x[2])은 내가 원하는게 아님
    # https://stackoverflow.com/questions/6618515/sorting-list-according-to-corresponding-values-from-a-parallel-list
    # print(newFatigue[0])
    # print(newFatigue[1])
    # print(newFatigue[2])  
    Z = [[x,y,z] for x,y,z in sorted(zip(newFatigue[0],newFatigue[1],newFatigue[2]),key=lambda x:-x[2])]
    # print(Z)
    
    i = 0
    while picks[0]>0:
        answer+=Z[i][0]
        picks[0]-=1
        i = i+5
        if i>len(minerals)-1 or sum(picks)==0:
            return answer
    while picks[1]>0:
        answer+=Z[i][1]
        picks[1]-=1
        i = i+5
        if i>len(minerals)-1 or sum(picks)==0:
            return answer
    while picks[2]>0:
        answer+=Z[i][2]
        picks[2]-=1
        i = i+5
        if i>len(minerals)-1 or sum(picks)==0:
            return answer
    