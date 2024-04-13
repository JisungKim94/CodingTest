import sys
input = sys.stdin.readline
N, M = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 한번 꼰 문젠데... dp로 접근한다는 생각을 좀 늦게했네
# 저번에 풀었던 이분탐색으로 꼬는 문제도 그렇고 생각을 잘 못떠올리는듯

move = [(0, 1), (1, 0)]
import collections
stack = collections.deque([(board[0][0],0,(0,0))])
dp = [[90001]*M for _ in range(N)]
dp[0][0] = 0
while stack:
    boost,ccost,(cr,cc) = stack.popleft()
    for dr,dc in move:
        for b in range(1,boost+1):
            nr,nc = cr+dr*b, cc+dc*b
            if 0<=nr<N and 0<=nc<M:
                if dp[nr][nc]>ccost+1:
                    dp[nr][nc] = ccost+1
                    stack.append((board[nr][nc],ccost+1,(nr,nc)))
print(dp[-1][-1])