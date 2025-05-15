def solution(routes):
    # 빨리 들어온 순서로 정렬
    routes.sort(key=lambda x: x[0])
    # print(routes)

    answer = 1
    pre_out = 30000
    for temp_in, temp_out in routes:
        # 제일 먼저 나가는 차보다 늦게 들어오는 차가 있으면
        if temp_in > pre_out:
            answer += 1
            pre_out = temp_out
        else:
            #
            pre_out = min(pre_out, temp_out)
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]) == 2)
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-30, 110]]) == 3)
print(
    solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-30, 110], [300, 1100]])
    == 3
)
