def solution(sequence):
    answer = sequence[0]
    l = 0
    r = 0
    prel, prer = -1, -1
    tempanswer = 0

    try:
        while l < len(sequence):
            if prer != r:
                if (r - l) % 2 == 0:
                    tempanswer = tempanswer + sequence[r]
                else:
                    tempanswer = tempanswer - sequence[r]
            else:
                tempanswer = -tempanswer + sequence[l - 1]
            prel, prer = l, r
            answer = max(abs(tempanswer), answer)
            print(tempanswer, answer, l, r)
            if abs(tempanswer) >= answer:
                r = r + 1
            else:
                if l < r:
                    l = l + 1
                else:
                    r = r + 1

    except:
        IndexError()
        # print("IE",l,r)

    return answer


solution([2, 3, -6, 1, 3, -1, 2, 4])
