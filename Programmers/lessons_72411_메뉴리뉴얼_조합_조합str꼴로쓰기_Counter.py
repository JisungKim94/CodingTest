from collections import Counter
from itertools import combinations, permutations


def solution(orders, course):
    answer = []
    temp_all_comb = []
    for course_length in course:
        for order in orders:
            temp_all_comb += combinations(sorted(order), course_length)
        # Counter는 어떤 배열에 동일한 원소가 몇 개 있는지 구해줌
        cnt_all_comb = Counter(temp_all_comb)
        if max(cnt_all_comb.values()) < 2:
            continue
        for comb in cnt_all_comb:
            if max(cnt_all_comb.values()) == cnt_all_comb.get(comb):
                # 조합 str 꼴로 만드는 방법
                answer.append("".join(comb))
        temp_all_comb = []

    # print(answer)
    return sorted(answer)


# print(
#     solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
#     == ["AC", "ACDE", "BCFG", "CDE"]
# )
# print(
#     solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
#     == ["ACD", "AD", "ADE", "CD", "XYZ"]
# )
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"])
