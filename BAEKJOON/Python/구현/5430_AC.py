import sys
from collections import deque

t = int(input())


def main():
    for i in range(t):
        p = sys.stdin.readline().rstrip()
        n = int(input())
        arr = sys.stdin.readline().rstrip()[1:-1].split(",")
        if arr[0] == "":
            arr = []
        arr = deque(arr)
        flag = 0
        for p_ in p:
            flag_ = 1
            if p_ == "R":
                flag += 1
            else:
                if arr:
                    if flag % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()
                else:
                    print("error")
                    flag_ = 0
                    break
        if flag % 2 == 0:
            pass
        else:
            arr.reverse()
        if flag_:
            print("[" + ",".join(arr) + "]")


if __name__ == "__main__":
    main()
