import collections


def solution(people, limit):
    # 문제 잘 읽어봐야 함... 보트가 작아서 두 명 밖에 못탄대
    # 쓰벌
    #
    # 신기하게도 그냥 list 쓰면 시간초과 뜨고 deque 사용해서 pop(0) 대신 popleft 사용하면 시간초과 안뜨네
    #
    answer = 0
    people = sorted(people)
    people = collections.deque(people)
    while people:
        if people[0] + people[-1] <= limit:
            people.popleft()
            if people:
                people.pop()
            answer = answer + 1
        else:
            people.pop()
            answer = answer + 1

    return answer


print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
print(solution([70, 80, 50], 300) == 2)
print(solution([40, 40, 40], 40) == 3)
print(solution([40, 100, 40], 140) == 2)
print(solution([40, 100, 40, 40], 140) == 2)
print(solution([40, 100, 40, 40], 100) == 3)
print(solution([10, 10, 10, 10, 10], 50) == 3)
print(solution([100, 500, 500, 900, 950], 1000) == 3)
print(solution([40, 50, 150, 160], 200) == 2)
