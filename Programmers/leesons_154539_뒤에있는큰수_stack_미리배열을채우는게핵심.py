def solution(numbers):
    # answer를 먼저 만들어놓고 idx로 접근하는게 핵심
    answer = [-1] * (len(numbers))
    # stack은 idx정보를 저장
    stack = []

    for idx, val in enumerate(numbers):
        # stack and numbers[stack[-1]] < numbers[idx]:
        # stack에 원소가 존재하고
        # 현재 number가 stack 맨 뒤에 값보다 클 때
        while stack and numbers[stack[-1]] < numbers[idx]:
            answer[stack.pop()] = numbers[idx]
        stack.append(idx)
    return answer


# print(solution([2, 3, 3, 5]) == [3, 5, 5, -1])
print(solution([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1])
