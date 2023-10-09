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


# 두번째풀이 dict pop을 몰랐어서 del을 사용했는데 어캐 잘 풀었다.
# dict.pop(i,None)을 공부하자
# if문 조건을 gemsets == dic.keys() 이걸로 했다가 시간초과가 났었는데 찾기 좀 힘들었음
# if len(gemsets) == len(dic.keys()): 이걸로 바꾸면 된다.


def solution(gems):
    answer = []
    gemsets = set(gems)
    dic = {}
    l, r = 0, -1
    minleng = 100001
    while l < len(gems):
        # if check(dic,gemsets):
        if len(gemsets) == len(dic.keys()):
            dic[gems[l]] = dic.get(gems[l], 0) - 1
            if dic.get(gems[l], 0) == 0:
                del dic[gems[l]]
            if minleng >= r - l:
                minleng = r - l
                answer.append([l, r])
            l += 1
        else:
            if r >= len(gems) - 1:
                if dic.get(gems[l], 0) > 0:
                    dic[gems[l]] -= 1
                l += 1
            else:
                r += 1
                dic[gems[r]] = dic.get(gems[r], 0) + 1
        # print(dic,l,r)
    # print(answer)
    answer.sort(key=lambda x: ((x[1] - x[0]), x[0]))
    answer = [answer[0][0] + 1, answer[0][1] + 1]
    return answer


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
