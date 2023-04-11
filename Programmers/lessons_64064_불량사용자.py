import itertools


def kjs(users, bid):
    for i in range(len(bid)):
        if len(users[i]) != len(bid[i]):
            return False

        for j in range(len(users[i])):
            if bid[i][j] == "*":
                continue
            if bid[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = 0
    temp = []

    for users in itertools.permutations(user_id, len(banned_id)):
        if not kjs(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in temp:
                temp.append(users)
    # print(temp)
    return len(temp)
