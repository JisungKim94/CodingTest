from math import ceil
from datetime import datetime


def solution(fees, records):
    answer = []
    records_in = {}
    records_minute = {}
    temp_fees = []

    ######################################################################
    ## 이 문제는 23:59 까지만 해서 아래와 같은 시간 계산 안 써도 가능했지만,
    ## 나중에 어려워지면 이거 써야할 수도 있음
    # time_1 = datetime.strptime("05:00:00", "%H:%M:%S")
    # time_2 = datetime.strptime("10:00:00", "%H:%M:%S")
    # time_interval = time_2 - time_1
    # print(time_interval)
    ######################################################################
    for i in records:
        i = i.split(" ")

        if i[2] == "IN":
            records_in[i[1]] = i[0]
            if records_minute.get(i[1]) == None:
                records_minute[i[1]] = 0
        else:
            in_ = records_in.pop(i[1])
            out_ = i[0]
            # print(out_, in_)
            temp_hour = (int(out_[0:2]) - int(in_[0:2])) * 60
            temp_min = int(out_[3:5]) - int(in_[3:5])
            temp = temp_hour + temp_min
            records_minute[i[1]] = records_minute[i[1]] + temp

    for i in records_in:
        in_ = records_in[i]
        out_ = "23:59"
        temp_hour = (int(out_[0:2]) - int(in_[0:2])) * 60
        temp_min = int(out_[3:5]) - int(in_[3:5])
        temp = temp_hour + temp_min
        records_minute[i] = records_minute[i] + temp

    for i in records_minute.keys():
        temp_fees.append((i, records_minute[i]))

    for i in sorted(temp_fees):
        if i[1] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((i[1] - fees[0]) / fees[2]) * fees[3])

    print(temp_fees)
    print(answer)
    return answer


# print(
#     solution(
#         [180, 5000, 10, 600],
#         [
#             "05:34 5961 IN",
#             "06:00 0000 IN",
#             "06:34 0000 OUT",
#             "07:59 5961 OUT",
#             "07:59 0148 IN",
#             "18:59 0000 IN",
#             "19:09 0148 OUT",
#             "22:59 5961 IN",
#             "23:00 5961 OUT",
#         ],
#     )
#     == [14600, 34400, 5000]
# )
# print(
#     solution(
#         [120, 0, 60, 591],
#         [
#             "16:00 3961 IN",
#             "16:00 0202 IN",
#             "18:00 3961 OUT",
#             "18:00 0202 OUT",
#             "23:58 3961 IN",
#         ],
#     )
#     == [0, 591]
# )
print(
    solution(
        [1, 461, 1, 10],
        ["00:00 1234 IN"],
    )
    == [14841]
)
