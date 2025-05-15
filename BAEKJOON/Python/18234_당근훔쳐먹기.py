import sys
input = sys.stdin.readline
N,T = map(int,input().split())
PbigWsmall = []
PsmallWbig = []
for _ in range(N):
    w,p = map(int,input().split())
    if p>=w:
        PbigWsmall.append((w,p))
    else:
        PsmallWbig.append((w,p))

# 오리는 그 텃밭에 N종류의 당근을 하나씩 심고 T일 동안 재배
# 당근 i(1 ≤ i ≤ N)는 처음에는 wi의 맛을 가지고 있고, 각 당근 i에 사용할 pi만큼 맛을 증가시켜주는 영양제가 당근 종류별로 T개씩 준비
# pi는 항상 wi이상의 값을 가지도록
# 오리는 각 당근 i에 대해 당근 i가 자리에 없다면 당근 i를 심고, 그렇지 않다면 당근 i에 영양제를 하나 준다.

# 꽉꽉나라에 놀러 온 토끼는 오리가 오전에만 당근을 관리한다는 사실을 알고 오리의 텃밭을 찾아가 당근을 훔쳐 먹을 계획을 세웠다. 
# 토끼는 위장이 작아서 하루에 최대 하나의 당근을 먹을 수 있고 당근을 먹지 않을 수도 있다. 또한 당근 하나를 먹기로 마음먹으면 남기지 않고 먹으며, 
# 오리와 마주치지 않기 위해 오후에만 텃밭에 찾아간다. 토끼는 자신이 먹은 당근의 맛의 합을 최대로 하고 싶어 한다. 
# T일 동안 토끼가 먹을 수 있는 당근의 맛의 합의 최댓값을 구해보자.


PbigWsmall.sort(key=lambda x: (x[1],x[0]+x[1]),reverse=1)
tokki = 0
stack = []
# w < p 라면... 계속 안먹다가 마지막에 쌓인거 터는게 최대이므로 아래와 같다. 
# w > p 여도 성립할까?? 이때는 먹고심고먹고심고가 이득일듯
for w,p in PsmallWbig:
    stack.append(w)
if stack:
    for _ in range(T-len(PbigWsmall)-1):
        # print(stack)
        idx = stack.index(max(stack))
        tokki += stack[idx]
        for i in range(len(PsmallWbig)):
            stack[i] += PsmallWbig[i][1]
        stack[idx] = PsmallWbig[idx][0]
# print(tokki)
idx = 0
for cnt in range(T-1,T-len(PbigWsmall)-1,-1):
    tokki += PbigWsmall[idx][0] + PbigWsmall[idx][1]*cnt
    idx+=1
    
print(tokki)
