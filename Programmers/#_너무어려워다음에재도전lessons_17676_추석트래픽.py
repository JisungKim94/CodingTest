def solution(lines):
    answer = 0
    S = []
    T_temp = []
    T = []
    U = []

    for line in lines:
        S.append((line).split(" ")[1])
        T_temp.append(((line).split(" ")[2]))

    for t in T_temp:
        temp = [i for i in t]
        temp.pop()
        T.append(float(("").join(temp)))

    for i, v in enumerate(S):
        U.append(S[i] + T[i])

    print(S, T)

    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]) == 1)
# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]) == 1)
# print(
#     solution(
#         [
#             "2016-09-15 20:59:57.421 0.351s",
#             "2016-09-15 20:59:58.233 1.181s",
#             "2016-09-15 20:59:58.299 0.8s",
#             "2016-09-15 20:59:58.688 1.041s",
#             "2016-09-15 20:59:59.591 1.412s",
#             "2016-09-15 21:00:00.464 1.466s",
#             "2016-09-15 21:00:00.741 1.581s",
#             "2016-09-15 21:00:00.748 2.31s",
#             "2016-09-15 21:00:00.966 0.381s",
#             "2016-09-15 21:00:02.066 2.62s",
#         ]
#     )
#     == 1
# )
