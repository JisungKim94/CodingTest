""" 
전체 탐색으론 아무리 효율성을 높여도 풀 수 없다.
two pointer라는 개념을 사용해야 하는데 map 구조를 이용하면 되고
python에선 map을 dictionary로 구성하기 때무넹 쉽게 만들 수 있따.

처음에 two pointer 개념을 생각하긴 했는데, map, dictionary를 사용 해
구현할 방법을 몰라서 못 품
"""

""" import collections


def solution(gems):
    set_gems = set(gems)
    # print("set_gems =", set_gems)
    for checkingLength in range(len(set_gems), len(gems) + 1):
        tmp_gems = collections.deque(gems[0:checkingLength])
        print(checkingLength, tmp_gems)
        for Starting in range(0, len(gems) + 1 - checkingLength):
            print(Starting, Starting + checkingLength - 1)

            # tmp_gems = set(gems[Starting : Starting + checkingLength])
            brk = True
            for k in set_gems:
                # print(k not in gems[Starting : Starting + checkingLength])
                if k not in tmp_gems:
                    brk = False
                    break
                else:
                    pass
            if brk:
                print(set_gems, tmp_gems)
                return [Starting + 1, Starting + checkingLength]
            else:
                if len(gems) <= Starting + checkingLength:
                    continue
                tmp_gems.popleft()
                tmp_gems.append(gems[Starting + checkingLength])
 """

""" 투 포인터 사용했지만, 모든 보석 key를 사용해서 시간초과
시간초과 막으려면 보고 있는 보석만 key에 남겨두고 del 시켜줘야 함"""
# def solution(gems):
#     answer = []
#     gems_set = set(gems)

#     l = 0
#     r = 0
#     gems_dic = {}
#     for i in gems_set:
#         gems_dic[i] = 0
#     gems_dic[gems[0]] = 1

#     while 1:
#         while 1:
#             if min(gems_dic.values()) > 0:
#                 answer.append((l, r))
#                 break
#             else:
#                 if r < len(gems) - 1:
#                     r = r + 1
#                     gems_dic[gems[r]] = gems_dic[gems[r]] + 1
#                 else:
#                     break

#         gems_dic[gems[l]] = gems_dic[gems[l]] - 1

#         if l < len(gems) - len(gems_set):
#             l = l + 1
#         else:
#             break

#         if min(gems_dic.values()) > 0:
#             answer.append((l, r))
#         else:
#             pass

#     answer = sorted(answer, key=lambda x: (x[1] - x[0]))
#     # print(answer)
#     # print([answer[0][0] + 1, answer[0][1] + 1])
#     return [answer[0][0] + 1, answer[0][1] + 1]


def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    l, r = 0, 0
    gem_dict = {gems[0]: 1}

    while l < len(gems) and r < len(gems):
        # 모든 보석 포함?
        if len(gem_dict) == size:
            if r - l < answer[1] - answer[0]:  # 최소 길이인지
                answer = [l, r]
            else:
                gem_dict[gems[l]] = gem_dict[gems[l]] - 1
                if gem_dict[gems[l]] == 0:
                    # del gem_dict[gems[left]]
                    gem_dict.pop(
                        gems[l], None
                    )  # Value 0, key 제거 해당 key가 없으면 error 대신 None 리턴
                l = l + 1

        else:
            r = r + 1
            if r == len(gems):
                break

            if gems[r] in gem_dict:  # 딕셔너리에 있으면 + 1
                gem_dict[gems[r]] = gem_dict[gems[r]] + 1
            else:  # 없으면 추가
                gem_dict[gems[r]] = 1

    return [answer[0] + 1, answer[1] + 1]


print(
    solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    == [3, 7]
)
print(
    solution(["DIA", "SAPPHIRE", "RUBY", "DIA", "RUBY", "EMERALD", "SAPPHIRE", "DIA"])
    == [4, 7]
)
print(solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]) == [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5])
