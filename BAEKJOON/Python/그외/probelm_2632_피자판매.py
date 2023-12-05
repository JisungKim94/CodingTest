import collections
import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
pizzaA = [int(input()) for _ in range(A)]
pizzaB = [int(input()) for _ in range(B)]
pizzaA=collections.deque(pizzaA)
pizzaB=collections.deque(pizzaB)
answer=0
# print(pizzaA,pizzaB)

caseA = collections.defaultdict(int)

for i in range(A):
    # print(pizzaA)
    tmp = 0
    for i in pizzaA:
        tmp+=i
        if 0<=tmp<=N:
            caseA[tmp]+=1
        else:
            break
    # 순환을 모듈로 하니까 헷갈려서 아래와 같이 구현
    pizzaA.append(pizzaA.popleft())
# 전체 합은 한 번만 있어야 하는데 중복 검사 하므로..
caseA[sum(pizzaA)] = 1
# 한 조각도 선택 안 해도 된다고 문제 조건에 있음
caseA[0]=1

caseB = collections.defaultdict(int)

for i in range(B):
    # print(pizzaB)
    tmp = 0
    for i in pizzaB:
        tmp+=i
        if 0<=tmp<=N:
            caseB[tmp]+=1
        else:
            break
    # 순환을 모듈로 하니까 헷갈려서 아래와 같이 구현
    pizzaB.append(pizzaB.popleft())
# 전체 합은 한 번만 있어야 하는데 중복 검사 하므로..
caseB[sum(pizzaB)] = 1
# 한 조각도 선택 안 해도 된다고 문제 조건에 있음
caseB[0]=1
# print(caseA,caseB)


# case로 2중 for문 통과 못 하는거 같음..
# caseA와 caseB의 합이 N이면 되는거니까 N으로 for문을 돌리면 통과!... 이게 좀 안떠올랐음...;
for i in range(N+1):
    j = N - i
    # print(i,j)
    if i in caseA and j in caseB:
        answer+=(caseA[i]*caseB[j])
print(answer)