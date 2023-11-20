def solution(genres, plays):
    answer = []
    check_genres_sum = {}
    check_genres = []

    # 딕셔너리 사용법
    for idx, val in enumerate(genres):
        # zip 수동으로 사용
        check_genres.append([idx, genres[idx], plays[idx]])
        # 장르별 재생횟수
        if val not in check_genres_sum:
            check_genres_sum[val] = plays[idx]
        else:
            check_genres_sum[val] = check_genres_sum[val] + plays[idx]

    # 딕셔너리 정렬 어캐 하게~?
    # https://codechacha.com/ko/python-sorting-dict/
    check_genres_sum = sorted(
        check_genres_sum.items(), key=lambda item: item[1], reverse=1
    )
    # 하나는 오름차 하나는 내림차일 경우
    check_genres = sorted(check_genres, key=lambda x: (x[2], -x[0]), reverse=1)
    # print(check_genres,check_genres_sum)

    for cgs in check_genres_sum:
        cnt = 0
        for cg in check_genres:
            if cgs[0] == cg[1] and cnt < 2:
                cnt += 1
                answer.append(cg[0])

    return answer


print(solution(["A", "B", "A", "A", "B"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(["B", "A"], [500, 600]) == [1, 0])
print(solution(["B"], [500]) == [0])
print(solution(["B", "A"], [600, 500]) == [0, 1])
print(solution(["A", "B"], [600, 500]) == [0, 1])
print(solution(["A", "A", "B"], [600, 500, 300]) == [0, 1, 2])
print(solution(["A", "B", "A"], [600, 500, 600]) == [0, 2, 1])
print(solution(["A", "B", "A"], [600, 500, 700]) == [2, 0, 1])
print(solution(["A", "A", "A"], [600, 500, 700]) == [2, 0])
print(solution(["A", "A", "A"], [3, 2, 1]) == [0, 1])
print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
    == [4, 1, 3, 0]
)
print(solution(["classic"], [2500]) == [0])
print(solution(["A", "B", "C"], [1, 2, 3]) == [2, 1, 0])
print(solution(["A", "B", "C", "D"], [1, 2, 3, 1]) == [2, 1, 0, 3])
print(solution(["A", "A", "B", "A"], [2, 2, 2, 3]) == [3, 0, 2])
print(solution(["A", "A", "B", "A"], [5, 5, 6, 5]) == [0, 1, 2])
print(solution(["A", "A", "B", "A", "B", "B"], [5, 5, 6, 5, 7, 7]) == [4, 5, 0, 1])
print(
    solution(
        ["classic", "pop", "classic", "classic", "classic"],
        [500, 1000, 400, 300, 200, 100],
    )
    == [0, 2, 1]
)
