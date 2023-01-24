from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cities = deque(cities)
    caches = []
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        while cities:
            temp = cities.popleft()
            temp = temp.lower()
            if len(caches) < cacheSize:
                if temp in caches:
                    answer = answer + 1
                else:
                    answer = answer + 5
                caches.append(temp)
            else:
                if temp in caches:
                    answer = answer + 1
                    caches.append(caches.pop(caches.index(temp)))
                else:
                    answer = answer + 5
                    caches.pop(0)
                    caches.append(temp)

    # print(answer)
    return answer


print(
    solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
        ],
    )
    == 50
)
print(
    solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
        ],
    )
    == 21
)
print(
    solution(
        2,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
    == 60
)
print(
    solution(
        5,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
    == 52
)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
print(solution(2, ["Jeju", "Jeju", "NewYork", "newyork"]) == 12)
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)
