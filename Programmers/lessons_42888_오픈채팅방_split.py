def solution(record):
    answer = []
    userinfo = {}
    for i, v in enumerate(record):
        v = (v).split(" ")
        if v[0] == "Change":
            userinfo[v[1]] = v[2]
        elif v[0] == "Enter":
            userinfo[v[1]] = v[2]

    for i, v in enumerate(record):
        v = (v).split(" ")
        if v[0] == "Enter":
            answer.append((userinfo.get(v[1]) + "님이 들어왔습니다."))
        elif v[0] == "Leave":
            answer.append((userinfo.get(v[1]) + "님이 나갔습니다."))

    return answer


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
    == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
)
