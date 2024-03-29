from itertools import combinations

# 엄청 어려웠다.. 일단 hash를 만들고 점수 오름차순으로 정리해서 미리 뽑아놓는 아이디어가 없었고
# 이후 이분탐색으로(lower bound) 검색하는것도 어려워


def solution(info, query):
    answer = []
    db = {}
    for i in info:  # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]  # 조건들만 모으고, 점수 따로
        score = int(temp[-1])
        for n in range(0, 5):  # 조건들에 대해 조합을 이용해서
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = (
                    conditions.copy()
                )  # 이렇게 안 하면 아래 tc[v] = "-" 에서 condition 변수 까지 바꿔어버림
                # t_c = conditions
                for v in c:  # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = "-"
                changed_t_c = "/".join(t_c)
                if changed_t_c in db:  # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)  # 같은 condition 조합에 걸리면서 점수가 다른 애들
                else:
                    db[changed_t_c] = [score]  # 새로운 condition 조합

    for value in db.values():  # 딕셔너리 내 모든 값 정렬
        value.sort()

    for q in query:  # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != "and"]
        qry_cnd = "/".join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
    == [1, 1, 1, 1, 2, 4]
)
