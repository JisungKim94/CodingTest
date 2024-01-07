N = int(input())
arr = list(map(int, input().split()))
total = [0] * N
answer = -1

# 조건을 만족하려면 아래와 같이 total이 구성되어야 한다.
# 1) 0번 부터 인덱스 i가 증가할 때 total[i] 값이 증가할 수 없다. (내 위에 x마리 있다했는데 아닌 경우는 거짓이므로)
# 2) total요소는 3이상일 수 없다. 냥이랑 토끼밖에 없응게
# 3) indexing이 마리수보다 많을수도 없다.
# 4) total의 2의 개수는 자리가 고정된 냥이와 토끼이므로 위치에 대한 경우의 수는 없어졌고 냥인지 토끼인지만 나뉘므로 *2씩 매번 한다.
# 5) 위 제한 조건을 만족하면서 total에 1이 있으면 1인 애들은 하나의 덩어리로 보고 이 세트가 냥이인지 토끼인지만 나뉘므로 *2를 한 번 한다.

try:
    for i in arr:
        total[i] += 1
    tmpanswer1 = 0
    tmpanswer2 = 0
    for i in range(N):
        if i<N-1 and total[i]<total[i+1]:
            tmpanswer1 = 0
            tmpanswer2 = 0
            break
        if total[i] > 2:
            tmpanswer1 = 0
            tmpanswer2 = 0
            break
        if total[i] == 2:
            tmpanswer2+=1
    if 1 in total[i]:
        tmpanswer1=1

    answer = 2**(tmpanswer2+tmpanswer1)
    if answer == 1:
        answer = 0
except:
    answer = 0


# print(total)
print(answer)