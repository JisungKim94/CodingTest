import sys
import math

# 쉬움 

T = int(input())
for _ in range(T):
    N = int(input())
    print(max(math.lcm(N,N-1,N-2), math.lcm(N,N-1,N-3), math.lcm(N-1,N-2,N-3)))
    