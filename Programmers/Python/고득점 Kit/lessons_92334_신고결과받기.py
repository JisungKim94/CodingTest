def solution(id_list, reports, k):
    answer = {}
    id_list_dic = {}
    report_manytimes_checker = []
    block_id = []
    for id in id_list:
        id_list_dic[id] = 0
        answer[id] = 0
    for report in reports:
        reportor = report.split(" ")[0]
        reported = report.split(" ")[1]
        if report not in report_manytimes_checker:
            id_list_dic[reported] = id_list_dic[reported] + 1
            report_manytimes_checker.append(report)
        # print(report_manytimes_checker)
        # for id_list in id_list_dic:
        if id_list_dic[reported] == k:
            block_id.append(reported)
    print(id_list_dic)
    print(block_id)
    for report in report_manytimes_checker:
        reportor = report.split(" ")[0]
        reported = report.split(" ")[1]
        if reported in block_id:
            answer[reportor] = answer[reportor] + 1

    answer = list(answer.values())
    print(answer)
    return answer


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
    == [2, 1, 1, 0]
)

# print(
#     solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
#     == [0, 0]
# )
