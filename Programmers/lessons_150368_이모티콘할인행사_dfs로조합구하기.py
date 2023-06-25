temp_price, join_ = 0, 0


def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    per = [10, 20, 30, 40]
    disc = [0] * (m)
    answer = []
    global temp_price, join_

    def dfs(idx):
        global temp_price, join_
        if idx == m:
            join_ = 0
            price, temp_price = 0, 0
            for uidx, u in enumerate(users):
                for didx, d in enumerate(disc):
                    if u[0] <= d:
                        temp_price += emoticons[didx] * (100 - d) // 100
                if temp_price >= u[1]:
                    join_ += 1
                else:
                    price += temp_price
                temp_price = 0
            answer.append([join_, price])
            return
        else:
            for p in per:
                disc[idx] = p
                dfs(idx + 1)

    dfs(0)

    answer.sort()
    # print(answer[-1])
    return answer[-1]
