def solution(n, results):
    #######################################################################################
    #######################################################################################
    # 아래와 같이 선언하면 각 행마다 배열이 선언됨
    # ranking = [[0] * n] * n
    # 이차원 배열을 만드려면 아래처럼 해야댐
    # ranking = [[0] * n for _ in range(n)]
    # 1번 방식대로 만들면 아래의 출력이 다음과 같이 나옴
    # ranking[0][0] = 1
    # [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    # 2번 방식으로 만들어야 원하는대로 나옴
    # [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    #######################################################################################
    #######################################################################################
    # print(result_2d)
    result_2d = [[0] * n for _ in range(n)]
    answer = 0
    for result in results:
        result_2d[result[0] - 1][result[1] - 1] = 1
    print(result_2d)

    # https://blog.naver.com/ndb796/221234427842
    # 1번이 2번을 이겼고 5번은 2번에게 졌으니까
    # through node = 2
    # start = 1
    # end= 5 인 연결이 완성된다.
    # through node
    for through in range(n):
        # start node
        for start in range(n):
            # end node
            for end in range(n):
                if result_2d[start][through] & result_2d[through][end] == 1:
                    result_2d[start][end] = 1
    print(result_2d)

    # 1번이 2번을 이겼다 = 2번과 1번의 승패는 결정이 되었다 이므로
    # [1,2]와 [2,1] 모두 1 로 처리 해 줘야 한당
    for i in range(n):
        for j in range(n):
            if result_2d[i][j] | result_2d[j][i]:
                result_2d[i][j] = 1
                result_2d[j][i] = 1

    for result in result_2d:
        if sum(result) == n - 1:
            answer = answer + 1

    print(answer)
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
