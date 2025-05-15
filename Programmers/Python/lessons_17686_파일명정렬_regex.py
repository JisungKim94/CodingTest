# 다른사람 풀이 보면 regex 사용 시 코드가 훨 간결해진다..
# 근디 공부하기 귀찮아잉


def solution(files):
    answer = []
    processing = []
    processed = []
    for i in files:
        for idx, val in enumerate(i):
            if val.isnumeric() == True:
                temp = i[:idx]
                # temp = temp.lower()
                processing = [temp]
                temp_ = i[idx:]
                break
        for idx_, val_ in enumerate(temp_):
            if val_.isnumeric() == False:
                processing.append(int(temp_[:idx_]))
                processing.append(temp_[:idx_])
                processing.append(temp_[idx_:])
                break
        if len(processing) == 1:
            processing.append(int(temp_))
            processing.append(temp_)

        processed.append(processing)

    processed = sorted(processed, key=lambda x: (x[0].lower(), x[1]))
    for i in processed:
        if len(i) == 4:
            answer.append(i[0] + i[2] + i[3])
        else:
            answer.append(i[0] + i[2])

    # print(answer)
    return answer


# print(
#     solution(
#         ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#     )
#     == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# )
print(
    solution(
        [
            "F-5 Freedom Fighter",
            "B-50 Superfortress",
            "A-10 Thunderbolt II",
            "F-14 Tomcat",
            "F-15",
        ]
    )
    == [
        "A-10 Thunderbolt II",
        "B-50 Superfortress",
        "F-5 Freedom Fighter",
        "F-14 Tomcat",
        "F-15",
    ]
)
