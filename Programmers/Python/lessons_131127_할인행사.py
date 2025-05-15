import collections

def solution(want, number, discount):
    answer = 0
    want_number = zip(want,number)
    want_number = dict(want_number)
    for i in range(len(discount)-9):
        # print(collections.Counter(discount[i: i +10]), dict(want_number))
        if collections.Counter(discount[i: i +10]) == dict(want_number):
            answer = answer+1
    # print(answer)
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])==3)
print(solution(["apple"],	[10],	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])==0)