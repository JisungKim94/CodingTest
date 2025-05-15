def transfer(in_, target, words, cnt, visited, checker):
    print("in :", in_)
    if in_ == target:
        checker.append(cnt)
        visited.pop()
        return checker
    wordsinfo = [0] * len(words)
    cnt = cnt + 1
    # something action in_ = new_in_
    for idx_1, word in enumerate(words):
        for idx_2 in range(len(word)):
            if word[idx_2] == in_[idx_2]:
                wordsinfo[idx_1] = wordsinfo[idx_1] + 1
    for i, v in enumerate(wordsinfo):
        if (v == len(in_) - 1) and (i not in visited):
            in_ = words[i]
            visited.append(i)
            transfer(in_, target, words, cnt, visited, checker)
    return checker


def solution(begin, target, words):
    answer = 0
    cnt = 0
    visited = []
    checker = []
    # words = copy.copy(words) # 뭔가 deepcopy랑 차이가 없어 보이지만, 만약 words 안에 list가 들어있는 뭐 2차원 배열같은 꼴이었다면 내부 list는 또 동시에 바뀜
    # words = words
    if transfer(begin, target, words, cnt, visited, checker):
        answer = min(transfer(begin, target, words, cnt, visited, checker))
    else:
        answer = 0
    print(answer)
    return answer


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)
