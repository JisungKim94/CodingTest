import sys
input = sys.stdin.readline
N = int(input())
mans = []
answer = 0
for _ in range(N):
    mans.append(int(input()))

mans.sort()
minmans = mans[0]
# print(mans)
# print(answer)

answer = mans[0] - 1
mans[0] = 1
# print(mans)
# print(answer)

idx = 1
temp = 0
while idx<len(mans):
    if mans[idx-1] == mans[idx]:
        pass
    else:
        temp = mans[idx] - mans[idx-1] - 1
        mans[idx] -= temp
        answer+=temp
    idx+=1
# print(mans)
print(answer)

