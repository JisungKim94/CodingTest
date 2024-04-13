import sys
input = sys.stdin.readline
TC = int(input())
# ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE
# 위 꼴의 arry를 만들고 저기 속하는 애들만 남기면서 진행하는데, 만약 남은 애들중에 없으면 숫자가 하나 더 있다고 생각해야할듯
# 음.. 근데 이러면 같은 숫자는 어떻게 해야할지 모르겠는데 ... -> 여기서 gg
# 다시보니 숫자마다 고유한 꼴들이 있어서 그걸 지워가면서 개수를 세면 된다. 시간제한도 널널함
# strnumbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
# 고유한 숫자
# Z : 0
# W : 2
# U : 4
# F : 위에서 4를 다 지웠으니 남은 F는 다 5
# X : 6
# V : 위에서 5를 다 지웠으니 남은 V는 다 7
# G : 8
# O : 1
# N : 9
# T : 3

                

strnumbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for tc in range(TC):
    temp = input().strip()
    answer = []
    if 'Z' in temp:
        cnt = temp.count('Z')
        for alph in strnumbers[0]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(0)
    if 'W' in temp:
        cnt = temp.count('W')
        for alph in strnumbers[2]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(2)
    if 'U' in temp:
        cnt = temp.count('U')
        for alph in strnumbers[4]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(4)
    if 'F' in temp:
        cnt = temp.count('F')
        for alph in strnumbers[5]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(5)
    if 'X' in temp:
        cnt = temp.count('X')
        for alph in strnumbers[6]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(6)
    if 'V' in temp:
        cnt = temp.count('V')
        for alph in strnumbers[7]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(7)
    if 'G' in temp:
        cnt = temp.count('G')
        for alph in strnumbers[8]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(8)
    
    if 'O' in temp:
        cnt = temp.count('O')
        for alph in strnumbers[1]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(1)
    if 'I' in temp:
        cnt = temp.count('I')
        for alph in strnumbers[9]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(9)
    if 'T' in temp:
        cnt = temp.count('T')
        for alph in strnumbers[3]:
            temp = temp.replace(alph,'',cnt)
        for _ in range(cnt):
            answer.append(3)
    answer.sort()
    for i in range(len(answer)):
        answer[i] = str(answer[i])
    answer = ''.join(answer)
    print(f"Case #{tc+1}:", answer)