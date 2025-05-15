from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    # append : [0, 1]을 append 하면 list에 [0,1] 추가
    # extend : [0, 1]을 extend 하면 list에 0, 1 추가
    combinations_ = []
    for i in range(1, col + 1):
        combinations_.extend(combinations(range(col), i))

    # 유일성 판단
    unique = []
    temp = []
    for combi in combinations_:
        # temp = [tuple(item[i] for i in combi) for item in relation]
        # print(temp)
        # temp = []
        # 위 temp랑 아래 temp랑 같은 표현
        for item in relation:
            for i in combi:
                tmp = tuple(item[i] for i in combi)
            temp.append(tmp)
        # print(temp)
        # 조합합친걸 temp list에 넣고 set으로 바꿔서 그게 row 길이만큼 나오는지 확인
        # row 길이만큼 나오면 그 조합으로는 유일성이 된다는거
        if len(set(temp)) == row:
            # unique list에 유일한 조합들 추가
            unique.append(combi)
        temp = []

    # 최소성 판단
    # discard : remove 같은건데 대신 존재하지 않는 set 지워도 error 안뜸
    # set type은 &교집합 |합집합 -차집합 가능
    # 추가 update, 삭제 remove 혹은 discard로 가능
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])

    return len(answer)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "1"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
    == 2
)
