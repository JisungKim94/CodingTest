import sys
input = sys.stdin.readline
# 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.
# 예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.
# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

# backtracking > 시간초과
# 앞이 다르고 뒤가 똑같으면 같은 계산을 두 번 하므로 e.g.) 1 2 6 12 24는 1 3 6 12 24와 앞에 1,2와 1,3만 다르고 뒤 세자리는 같다.
# memoization 사용, 딕셔너리로 구현
# 메모이제이션 하면 엄청 빨라보이는데.. 시간초과 뜨네 여전히;; 여기선 빠른데 왜 백준에선 느린지 모르겠다.
import sys
input = sys.stdin.readline
# 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.
# 예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.
# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

# backtracking > 시간초과
# 앞이 다르고 뒤가 똑같으면 같은 계산을 두 번 하므로 e.g.) 1 2 6 12 24는 1 3 6 12 24와 앞에 1,2와 1,3만 다르고 뒤 세자리는 같다.
# memoization 사용, 딕셔너리로 구현
# 메모이제이션 하면 엄청 빨라보이는데.. 시간초과 뜨네 여전히;; 여기선 빠른데 왜 백준에선 느린지 모르겠다.

import sys
input = sys.stdin.readline
# 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.
# 예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.
# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

# backtracking > 시간초과
# 앞이 다르고 뒤가 똑같으면 같은 계산을 두 번 하므로 e.g.) 1 2 6 12 24는 1 3 6 12 24와 앞에 1,2와 1,3만 다르고 뒤 세자리는 같다.
# memoization 사용, 딕셔너리로 구현
# 메모이제이션 하면 엄청 빨라보이는데.. 시간초과 뜨네 여전히;; 여기선 빠른데 왜 백준에선 느린지 모르겠다.
import sys
input = sys.stdin.readline
# 각 숫자는 이전에 고른 수보다 적어도 2배가 되도록 고르기 때문이다.
# 예를 들어, n=4, m=10일 때, 선영이는 다음과 같이 고를 수 있다.
# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

# backtracking > 시간초과
# 앞이 다르고 뒤가 똑같으면 같은 계산을 두 번 하므로 e.g.) 1 2 6 12 24는 1 3 6 12 24와 앞에 1,2와 1,3만 다르고 뒤 세자리는 같다.
# memoization 사용
# 딕셔너리로 해도 시간초과뜸..;; 아마 if (numb,idx) in memo: 에서 뜨는거 같음
# 테이블로 해보자
def dfs(numb, idx, memo):
    if memo[numb][idx]:
        return memo[numb][idx]
    
    if idx == n - 2:
        memo[numb][idx] = (m - numb * 2 + 1)
        return memo[numb][idx]

    count = 0
    for nnumb in range(numb * 2, m + 1):
        if m < nnumb * 2**(n-idx-2):
            break
        count += dfs(nnumb, idx + 1, memo)
    
    memo[numb][idx] = count
    return count

TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    answer = 0
    memo = [[0]*n for _ in range(m+1)]
    
    if n == 1:
        answer = m
    else:
        for i in range(1, m + 1):
            if m < i * 2**(n-1):
                break
            answer += dfs(i, 0, memo)

    print(answer)

