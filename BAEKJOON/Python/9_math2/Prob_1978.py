Case = int(input())     # 막상 코드에서 사용하진 않는데 case입력 필요해서 넣음
num_list = list(map(int, input().split(' ')))

counting = 0

for i in num_list:
    cnt = 0
    if(i == 1):
        continue
        # 1은 예외처리해서 continue로 빼준다.
    for j in range(2, i + 1):
        if(i % j == 0):
            cnt += 1
            # 뭔 수로 나누든 나머지가 없으면 소수니까 cnt 1up
    if(cnt == 1):
        counting += 1
print(counting)