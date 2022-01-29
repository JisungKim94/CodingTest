import collections


def solution(priorities, location):
    # stack_0 = collections.deque(priorities)
    # stack_1 = collections.deque(range(len(priorities)))
    stack = [(i, p) for i, p in enumerate(priorities)]
    stack = collections.deque(stack)
    # 위에껄 한방에 하려면
    # stack = [(i, p) for i, p in enumerate(priorities)]
    # 대신 이렇게 하려면 while문 안에 if문에 max를 못 쓰는데..
    # if any(cur[1] < q[1] for q in queue):
    # 위의 방식을 사용해서 해결 가능
    # any는 괄호 안의 반복문 중 하나라도 True면 True를 반납
    # empty거나 all False면 False 반납
    answer = 0
    # print(stack_1)
    while stack:
        # cur_0 = stack_0.popleft()
        # cur_1 = stack_1.popleft()
        cur = stack.popleft()
        try:
            if any(cur[1] < s[1] for s in stack):
                stack.append(cur)
            else:
                answer = answer + 1
                if cur[0] == location:
                    # print(answer)
                    break
        except ValueError:
            answer = answer + 1
        # print(stack_1)
    # print(stack_1.popleft())

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([2, 1, 0, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([9, 9, 1, 9, 9, 9], 2))
