import sys
input = sys.stdin.readline
S = input().strip()
T = input().strip()
stack = []
length = len(T)
# stack 문제였음~!

for i in S:
    stack.append(i)
    if len(stack)>=length and "".join(stack[-length:]) == T:
        for _ in range(length):
            stack.pop()
print("".join(stack))