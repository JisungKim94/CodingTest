# ==============================================================
# 내 풀이
# ==============================================================
def solution(clothes):
    answer = 1
    info = []
    # 이거 다른 사람 코드 보고 고치자 이상한게 짠거 같음
    for idx, clth in enumerate(clothes):
        if clth[1] not in info:
            info.append(clth[1])
    info_ = [0] * len(info)
    # print(info)
    for idx, clth in enumerate(clothes):
        for i in range(len(info)):
            if clth[1] == info[i]:
                info_[i] = info_[i] + 1
    # print(info_)

    # 이건 못찾았음... 멍충멍충
    # 내가 찾은 풀이는 e.g. 총 a개 b개 c개 있으면 (a + b + c) + (ab + bc + ca) + abc 이게 답이라는 거 였는데...
    # 이걸 구현을 못했었음 위 식은 (a+1)(b+1)(c+1)-1 로 표현할 수 있음.
    for i in info_:
        answer = answer * (i + 1)
    answer = answer - 1
    return answer


solution(
    [
        ["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"],
        ["abc", "ddd"],
    ]
)

# ==============================================================
# 내 풀이 방법을 깔끔하게 쓴 거
# ==============================================================
def solution(clothes):
    # dictionary를 이용한 풀이
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 1
        else:
            clothes_type[t] += 1
    print(clothes_type)
    cnt = 1

    # 이건 못찾았음... 멍충멍충
    # 내가 찾은 풀이는 e.g. 총 a개 b개 c개 있으면 (a + b + c) + (ab + bc + ca) + abc 이게 답이라는 거 였는데...
    # 이걸 구현을 못했었음 위 식은 (a+1)(b+1)(c+1)-1 로 표현할 수 있음.
    for num in clothes_type.values():
        cnt *= num + 1

    return cnt - 1


print(
    solution(
        [
            ["yellowhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["green_turban", "headgear"],
            ["abc", "ddd"],
        ]
    )
)
