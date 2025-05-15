import sys
input = sys.stdin.readline
def stupid(A,B):
    n = 1
    if A<B:
        while 1:
            if A*(n+1)>B:
                break
            n+=1
        nA = A
        nB = B - A*n
    else:
        while 1:
            if B*(n+1)>A:
                break
            n+=1
        nA = A - B*n
        nB = B
    return nA,nB

while 1:
    A,B = map(int,input().split())
    if A==0 and B==0:
        break
    answer = 0
    while 1:
        nA,nB = stupid(A,B)
        print(nA,nB)
        answer+=1
        if nA == 0 or nB == 0:
            break
        A,B = nA,nB
    print(answer)

