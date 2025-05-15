def solution(n):
    answer = ""

    if n <= 3:
        return "124"[n - 1]
    else:
        n_div, n_mod = divmod(n - 1, 3)
        return solution(n_div) + "124"[n_mod]


print(solution(1) == "1")
# print(solution(2) == "2")
print(solution(3) == "4")
# print(solution(4) == "11")
# print(solution(10) == "41")
# print(solution(11) == "42")
print(solution(12) == "44")
print(solution(13) == "111")
print(solution(14) == "112")
print(solution(16) == "121")
