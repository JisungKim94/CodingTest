def solution(a):
    answer = 0
    v_min = a[0]
    for i, v in enumerate(a[: a.index(min(a))]):
        v_min = min(v, v_min)
        if v <= v_min:
            # print(v,v_min)
            answer = answer + 1

    if a.index(min(a)) != len(a) - 1:
        x = a[a.index(min(a)) :]
        x.reverse()
        v_min = x[0]
        # print(x)
        for i, v in enumerate(x):
            v_min = min(v, v_min)
            if v <= v_min:
                # print(v,v_min)
                answer = answer + 1
    else:
        answer = answer + 1

    return answer
