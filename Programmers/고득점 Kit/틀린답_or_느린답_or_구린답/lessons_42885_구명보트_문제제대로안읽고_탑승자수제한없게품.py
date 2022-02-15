def solution(people, limit):
    # 문제 잘 읽어봐야 함... 보트가 작아서 두 명 밖에 못탄대
    # 쓰벌
    # 그리고 마지막 두 개 case 만족 못 하는 이유는 아래 sorting을 오름차 내림차 어캐할지 고민을 안하고 해서 그럼
    # 무거운 애들부터 태워서 최적화를 해 줘야 하는데 가벼운 애들부터 태우면 40, 50, 150, 160 같은 경우에
    # 40, 50이 타버려서 안대는거
    # 40,160, 50,150  이렇게 타야대는데 40,50이 타버리기 때문에 소팅을 잘 해줘야댐
    answer = 0
    people = sorted(people, reverse=1)
    boat = []
    minumum = people[-1]

    while people:
        for i in people:
            if sum(boat) <= limit - minumum:
                boat.append(people.pop())
                if people:
                    minumum = people[-1]
            if sum(boat) > limit - minumum:
                boat = []
                answer = answer + 1
                break

    if answer == 0:
        answer = 1
    # print(answer)
    return answer


print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
print(solution([70, 80, 50], 300) == 1)
print(solution([40, 40, 40], 40) == 3)
print(solution([40, 100, 40], 140) == 2)
print(solution([40, 100, 60, 40], 140) == 2)
print(solution([40, 100, 50, 50], 100) == 3)
print(solution([100, 500, 500, 900, 950], 1000) == 3)
print(solution([40, 50, 150, 160], 200) == 2)
