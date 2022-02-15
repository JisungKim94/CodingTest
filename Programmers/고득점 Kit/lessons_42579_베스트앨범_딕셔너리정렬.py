def solution(genres, plays):
    answer = []
    check_genres_sum = {}
    check_genres = []

    # 딕셔너리 사용법
    for idx, val in enumerate(genres):
        check_genres.append([idx, genres[idx], plays[idx]])
        if val not in check_genres_sum:
            check_genres_sum[val] = plays[idx]
        else:
            check_genres_sum[val] = check_genres_sum[val] + plays[idx]
    # print(check_genres_sum)
    # print(check_genres)
    # 딕셔너리 정렬 어캐 하게~?
    # https://codechacha.com/ko/python-sorting-dict/
    check_genres_sum = sorted(
        check_genres_sum.items(), key=lambda item: item[1], reverse=1
    )
    check_genres = sorted(check_genres, key=lambda item: item[2], reverse=1)
    # print(check_genres_sum)
    # print(check_genres)

    for genres_sum in check_genres_sum:
        temp_0 = genres_sum[0]
        cnt = 0
        for idx, check_val in enumerate(check_genres):
            if check_val[1] == temp_0 and cnt < 2:
                answer.append(check_val[0])
                cnt = cnt + 1

    print(answer)
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
