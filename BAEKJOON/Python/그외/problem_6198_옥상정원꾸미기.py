import collections
N = int(input())
building = [int(input()) for _ in range(N)]
stack = collections.deque([])
answer = 0

for b in building:
    while stack and stack[-1]<=b:
        stack.pop()
    stack.append(b)
    # print("높이가 stack[-1](=b)인 건물을 내려다볼 수 있는 건물들" ,stack)
    answer += len(stack)-1

print(answer)