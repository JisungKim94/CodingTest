numbers = [1, 2]
target = 3


def dfs(numbers, target, list__, size, answer):
    if len(list__) == size:
        if sum(list__) == target:
            return 1
        else:
            return 0
    else:
        # pop이랑 append 재귀로 불리는 dfs 위치가 중요한데 디게 헷갈리네...
        A = numbers.pop(0)
        for i in [-1, 1]:
            list__.append(i * A)
            answer = answer + dfs(numbers, target, list__, size, answer)
            list__.pop()
        numbers.append(A)
        return answer


def solution(numbers, target):
    answer = 0
    list__ = []
    answer = dfs(numbers, target, list__, len(numbers), answer)
    return answer


print(solution(numbers, target))
