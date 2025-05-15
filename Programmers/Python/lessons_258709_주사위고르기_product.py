import itertools

    
#   A팀 최소~최대가 있다고 치고 B팀 최소~최대가 있다고 칠 때 조합은 총 6**n//2개 나올거고
#   A의 최대와 B의 최소 뭐 이런식으로 비교하면서 같은게 나오면 그기까지 이길 수 있는거니까 서로 곱하면 될듯

def solution(dice):
    answer = []
    sumdice = []
    for i in range(len(dice)):
        dice[i].sort
    
    cases = list(itertools.combinations(range(len(dice)),len(dice)//2))
    maxcnt = 0
    for case in cases:
        teamA,teamB = [],[]
        for i in range(len(dice)):
            if i in case:
                teamA.append(dice[i])
            else:
                teamB.append(dice[i])
        
        scoreA,scoreB = [],[]
        for s in itertools.product(*teamA):
            scoreA.append(sum(s))
        for s in itertools.product(*teamB):
            scoreB.append(sum(s))
        scoreA.sort()
        scoreB.sort()
        cnt = 0
        i,j = 0,0
        # print(scoreA)
        # print(scoreB)
        while i<len(scoreA) and j<len(scoreB):
            if scoreA[i]>scoreB[j]:
                j+=1
            else:
                cnt+=j
                i+=1
        if i<len(scoreA):
            cnt+=(len(scoreA)-i)*j
        # print(cnt,case)
        if cnt>maxcnt:
            maxcnt=cnt
            answer = sorted(list(case))
    for i in range(len(answer)):
        answer[i]+=1
    return answer