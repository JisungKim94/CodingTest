# 이렇게 하면 stones가 내림차순일 경우 if문을 계속 돌리므로 효과가 사라지고
# 시간초과가 뜸 TC 13번
# def solution(stones, k):
#     answer = 200000001

#     temp_answer = max(stones[0:k])
#     for i in range(len(stones) - k + 1):
#         if stones[i - 1] == temp_answer:
#             temp_answer = max(stones[i : i + k])
#         answer = min(answer, temp_answer)
#         # print(answer)

#     return answer

# 이분탐색으로 풀어야 함
# l,r은 각각 돌을 밟을 수 있는 값
# stone을 순서대로 보면서 mid보다 작은게 연속으로 k개 나오면
# break 하고 r을 줄임
# 끝까지 안나오면 l을 늘리고 answer를 업데이트
def solution(stones, k):
    l, r = 0, max(stones)
    answer = 1
    while l <= r:
        mid = (l + r) // 2
        zero_stone = 0
        binary_search = True
        for stone in stones:
            if stone < mid:
                zero_stone += 1
                if zero_stone == k:
                    binary_search = False
                    break
            else:
                zero_stone = 0
        if binary_search:
            answer = max(answer, mid)
            l = mid + 1
        else:
            r = mid - 1
    return answer
