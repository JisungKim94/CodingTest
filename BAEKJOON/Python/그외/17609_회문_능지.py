import sys

# 투포인터 문제인건 알았으나..
# 능지 이슈로 틀림...
# 아래는 구글링으로 얻은 답


# skip된 문자열이 회문인지 판단하는 함수
def is_palindrome(word, left, right):
	while left < right:
		if word[left] != word[right]:
			return False
		left += 1
		right -= 1
	return True
    
# 다른 문자가 나타났을 때, 해당 문자를 skip하고 비교해서 회문이면 유사 회문으로 판단
# 그렇지 않으면 일반문으로 판단함
def is_pseudo(word):
	left, right = 0, len(word)-1
	while left < right:
		if word[left] != word[right]:
			return is_palindrome(word, left+1, right) or is_palindrome(word, left, right-1)
		left += 1
		right -= 1
	return False
    
    
t = int(sys.stdin.readline())
for _ in range(t):
	word = list(sys.stdin.readline().rstrip())
	if is_palindrome(word, 0, len(word)-1):
		print(0)
	elif is_pseudo(word):
		print(1)
	else:
		print(2)
