numbers = [1, 1, 1, 1, 1]
target = 3

# 재귀를 이용한 dfs 트리를 아래로 파고 옆으로 한칸 옮기는 식
# dfs 함수 내에서 다시 dfs함수를 부르는 재귀 방식
def dfs(array, numbers, target, size):
    answer = 0
    if len(array) == size:
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        A = numbers.pop(0)
        for i in [1, -1]:
            array.append(A * i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(A)
        return answer


def solution(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer


import collections

# stack을 이용한 bfs 트리를 가로로 채우고 한칸 아래로 내리는 식
def solution(numbers, target):
    answer = 0
    # collections.deque를 이용해 (0,0) 노드 하나 만듬
    stack = collections.deque([(0, 0)])
    while stack:
        # deque 모듈은 popleft랑 appendleft를 사용 (걍 팝 푸시 하면 안드감)
        current_sum, num_idx = stack.popleft()

        # else에서 두 개 씩 stack에 추가하고
        # 위에pop left에서 한개씩 stack에서 빼서 확인함
        # 근데 numbers에 있는거 다 넣어봤으면(num_idx == 5)
        # 그때부턴 추가는 안함
        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer


print(solution(numbers, target))
