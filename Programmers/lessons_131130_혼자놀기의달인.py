def solution(cards):
    answer = 0

    group = []
    visited = []
    for i in cards:
        if i not in visited:
            group.append([])
            while i not in group[-1]:
                group[-1].append(i)
                visited.append(i)
                i = cards[i - 1]

    group.sort(key=lambda x: len(x))

    if len(group) == 1:
        answer = 0
    else:
        answer = len(group[-1]) * len(group[-2])

    return answer
