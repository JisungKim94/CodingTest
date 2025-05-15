import collections


def solution(enroll, referral, seller, amount):
    enroll = collections.deque(enroll)
    referral = collections.deque(referral)
    enroll.appendleft("-")
    referral.appendleft("center")
    answer = []
    tree = {}
    earn = {}
    for enr, ref in zip(enroll, referral):
        earn[enr] = 0
        tree[enr] = ref
    # print(tree)

    # print(sales)
    for sel, amo in zip(seller, amount):
        amo = amo * 100
        won = int(0.1 * amo)
        earn[sel] = earn[sel] + amo
        i = tree[sel]
        while i != "center":
            earn[i] = earn[i] + won
            won = int(0.1 * won)
            earn[i] = earn[i] - won
            i = tree[i]
            if won < 1:
                break
        earn[sel] = earn[sel] - int(0.1 * amo)

        # print(earn,"\n")

    del earn["-"]
    for i in earn:
        answer.append(earn[i])

    return answer
