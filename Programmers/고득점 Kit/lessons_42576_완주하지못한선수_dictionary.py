# participant = ["leo", "kiki", "eden"]
participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["eden", "kiki"]
completion = ["stanko", "ana", "mislav"]

answer = {}
for i in participant:
    answer[i] = answer.get(i, 0) + 1
for j in completion:
    answer[j] -= 1
for k in answer:
    if answer[k] >= 1:
        print(k)
