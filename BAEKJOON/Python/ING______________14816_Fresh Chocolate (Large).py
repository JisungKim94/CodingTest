import sys
input = sys.stdin.readline
T = int(input())

# googling 해서 찾은 풀이
def fresh_chocolate(N, P, groups):
    remainders = [0] * P
    for pieces in groups:
        remainders[pieces % P] += 1

    if P == 2:
        return remainders[0] + (remainders[1] + 1) // 2

    elif P == 3:
        groups = remainders[0] + min(remainders[1], remainders[2])
        remaining = abs(remainders[1] - remainders[2])
        groups += remaining // 3
        if remaining % 3 != 0:
            groups += 1
        return groups

    elif P == 4:
        groups = remainders[0]
        pairs = min(remainders[1], remainders[3])
        groups += pairs
        remainders[1] -= pairs
        remainders[3] -= pairs
        groups += remainders[2] // 2
        remainders[2] %= 2
        if remainders[2] > 0:
            groups += 1
            if remainders[1] >= 2:
                remainders[1] -= 2
            elif remainders[3] >= 2:
                remainders[3] -= 2
            else:
                remainders[1] = 0
                remainders[3] = 0
        groups += remainders[1] // 4
        if remainders[1] % 4 != 0:
            groups += 1
        groups += remainders[3] // 4
        if remainders[3] % 4 != 0:
            groups += 1
        return groups

for tc in range(T):
    # answer = 0
    N,P = map(int,input().split())
    groups = list(map(int,input().split()))
    # arranged = [[] for _ in range(P)]
    # for i in groups:
    #     arranged[i%P].append(i)
    
    # answer += len(arranged[0])
    # arranged[0] = []
    # left = 0
    # flag = 1
    # while flag:
    #     flag = 0
    #     if left == 0:
    #         for i in range(len(arranged)):
    #             if len(arranged[i]) != 0:
    #                 left = P-arranged[i].pop()%P
    #                 answer+=1
    #                 break
    #     else:
    #         if len(arranged[left]) != 0:
    #             arranged[left].pop()
    #             left = 0
    #         else:
    #             for i in range(len(arranged)):
    #                 if len(arranged[i]) != 0:
    #                     left = P-(arranged[i].pop()-left)%P
    #                     break
            

    #     for i in range(len(arranged)):
    #         if len(arranged[i])==0: pass
    #         else: flag = 1
    # print(fresh_chocolate(N,P,groups))
    print(f"Case #{tc+1}:", fresh_chocolate(N,P,groups))
                
                
                
            
    
    
    


# P=3 이고 
# 투어 그룹이 5명이 왔으면 2개의 팩을 까서 하나씩 준다. 
# 그리고 다음 투어 그룹이 6명이 왔으면 남은 하나를 주고 팩 2개를 더 까서 준다.
# 다음 투어 그룹은 4명이면 남은거 하나에 1팩
# 다음 투어그룹도 4명이면 2팩개봉
# 이때 까여있는 초콜렛이 있으면 어차피 새거 깔 예정이어도 새거를 쓰면 안된다.

# 일단 나눠 떨어지는 애들 먼저 다 맥임