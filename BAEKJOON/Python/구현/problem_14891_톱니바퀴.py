# 입력
import sys
from collections import deque
input = sys.stdin.readline
wheel = [deque(list(map(int,input().rstrip()))) for _ in range(4)] # 톱니 상태 저장
k = int(input())
answer = 0
print(wheel)
for _ in range(k):
	n, isCW = map(int,input().split())
	n = n-1
	tmp = [0,0,0,0]
	tmp[n] = isCW
	n_ = n
	while n_+1<4:
		if wheel[n_][2] != wheel[n_+1][6]:
			tmp[n_+1] = tmp[n_]*-1
		else:
			pass
		n_+=1
	n_ = n
	while n_-1>=0:
		if wheel[n_][6] != wheel[n_-1][2]:
			tmp[n_-1] = tmp[n_]*-1
		else:
			pass
		n_-=1
	print(tmp)
	for idx,v in enumerate(tmp):
		if v == 0:
			pass
		elif v == 1:
			wheel[idx].appendleft(wheel[idx].pop())
		else:
			wheel[idx].append(wheel[idx].popleft())
	print(wheel)
if wheel[0][0] == 1:
	answer+=1
if wheel[1][0] == 1:
	answer+=2
if wheel[2][0] == 1:
	answer+=4
if wheel[3][0] == 1:
	answer+=8
print(answer)