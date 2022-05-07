def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_list_who_i_report = {}
    num_of_reported = {}
    report = set(report)  # 중복제거

    for id in id_list:
        user_list_who_i_report[id] = set()
        num_of_reported[id] = int()

    block_id = []  # 강퇴당할 유저목록

    for r in report:
        do_report, be_reported = r.split()  # 이렇게 하는게 간지

        num_of_reported[be_reported] += 1  # 신고당한 : 신고당한 횟수
        user_list_who_i_report[do_report].add(be_reported)
        # 신고한애 : 신고당한애

        # k번 당했으면 block_id에 넣어
        if num_of_reported[be_reported] == k:
            block_id.append(be_reported)
    for b in block_id:
        for i in range(len(id_list)):
            if b in user_list_who_i_report[id_list[i]]:
                # dict에서 dict[key] 하면 value를 출력함.
                # key = id_list일 때 정지먹을넘이 value에 있는지 확인
                # i는 id_list 에서의 index 역할을 하므로
                answer[i] += 1

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
