# 내 풀이


def solution(lottos, win_nums):
    answer = []
    lowest_ranking = 0
    highest_ranking = 0
    for num in lottos:
        if num in win_nums:
            lowest_ranking = lowest_ranking + 1
        if num == 0:
            highest_ranking = highest_ranking + 1
    highest_ranking = highest_ranking + lowest_ranking

    highest_ranking, lowest_ranking = 7 - highest_ranking, 7 - lowest_ranking
    if highest_ranking > 6:
        highest_ranking = 6
    if lowest_ranking > 6:
        lowest_ranking = 6

    answer.append(highest_ranking)
    answer.append(lowest_ranking)
    # print(answer)
    return answer


# 개쩌는 답
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5])
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6])
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1])
