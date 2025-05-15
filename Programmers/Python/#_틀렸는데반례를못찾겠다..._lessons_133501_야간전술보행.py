def solution(distance, scope, times):
    answer = distance
    # print(sorted(list(zip(scope, times))))
    for s, t in sorted(list(zip(scope, times))):
        s = sorted(s)
        dist1 = (s[0]) % (t[0] + t[1])
        dist2 = (s[1]) % (t[0] + t[1])
        # print(dist1, dist2)
        if s[1]-s[0] > t[0]+t[1]:
            answer = (s[0]+(t[0] + t[1] - dist1 + 1))
            break
        else:
            if (dist1 > t[0] or dist1 == 0) and (dist2 > t[0] or dist2 == 0):
                pass
            else:
                if dist1 > t[0]:
                    answer = (s[0] + (t[0] + t[1]) - dist1 + 1)
                elif dist1 == 0:
                    answer = (s[0] + 1)
                else:
                    answer = (s[0])
                break

    # print(answer)
    return answer


print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]) == 8)
print(solution(10, [[3, 4], [9, 11]], [[2, 5], [3, 1]]) == 9)
print(solution(12, [[8, 7], [6, 4], [10, 11]], [[2, 2], [2, 4], [3, 3]]) == 12)
print(solution(829, [[821, 763], [569, 740], [295, 24], [378, 391], [456, 531], [353, 366]], [[1,4],[6,8],[5,8],[7,2],[9,5],[6,9]]) == 27)