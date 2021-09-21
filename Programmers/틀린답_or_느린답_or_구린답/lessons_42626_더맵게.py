scoville = [1, 2, 3, 9, 10, 12]
# scoville = [1, 2, 3, 0, 0]
K = 7


def solution(scoville, K):
    answer = 0
    while True:
        first = scoville[scoville.index(min(scoville))]
        scoville.pop(scoville.index(min(scoville)))
        second = scoville[scoville.index(min(scoville))]
        scoville.pop(scoville.index(min(scoville)))

        scoville.append(first + second * 2)

        answer = answer + 1
        if len(scoville) < 2 or min(scoville) >= K:
            if min(scoville) < K:
                answer = -1
            break

    return answer


print(solution(scoville, K))
