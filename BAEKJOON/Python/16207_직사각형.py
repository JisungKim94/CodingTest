import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

# 음.. 그냥 떠오르는 방식으로 하면 될거같은데 구현문젠가
A.sort()
# print(N,A)

temp_rec = []
answers = []
while A:
    line = A.pop()
    if len(temp_rec) == 0:
        temp_rec.append(line)
    else:
        if (temp_rec[-1]-line) == 0:
            temp_rec.append(line)
        elif (temp_rec[-1]-line) == 1:
            temp_rec[-1]-=1
            temp_rec.append(line)
        else:
            temp_rec = []
            temp_rec.append(line)
    if len(temp_rec) == 2:
        answers.append(temp_rec[0])
        temp_rec = []
# print(answers)
answer = 0
for i in range(len(answers)):
    if i%2 == 0:
        temp1 = answers[i]
    else:
        answer += temp1 * answers[i]
print(answer)