def solution(numbers, hand):
    answer = []
    L_pre = 10
    R_pre = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer.append("L")
            L_pre = i
        elif i in [3, 6, 9]:
            answer.append("R")
            R_pre = i
        elif i in [2, 5, 8, 0]:
            i = 11 if i == 0 else i
            if sum(divmod(abs(i - L_pre), 3)) < sum(divmod(abs(i - R_pre), 3)):
                answer.append("L")
                L_pre = i
            elif sum(divmod(abs(i - L_pre), 3)) > sum(divmod(abs(i - R_pre), 3)):
                answer.append("R")
                R_pre = i
            elif sum(divmod(abs(i - L_pre), 3)) == sum(divmod(abs(i - R_pre), 3)):
                if hand == "right":
                    answer.append("R")
                    R_pre = i
                elif hand == "left":
                    answer.append("L")
                    L_pre = i

    answer = "".join(answer)
    # print(answer)
    return answer


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
