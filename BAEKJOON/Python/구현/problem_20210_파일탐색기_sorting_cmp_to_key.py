import sys
input = sys.stdin.readline
from functools import cmp_to_key

# 구현문젠데 쪼금 빡세다..
# 못품 https://latte-is-horse.tistory.com/359 참고했음

n = int(input())
files = [input().strip() for _ in range(n)]
def strsplit(file):
    # 여기 구현을 string까지 숫자처럼 묶었는데 그렇게 하면 구현이 좀 힘들어지는듯 ㅠㅠ;;
    l,r = 0,0
    ret = []
    while r<len(file):
        if file[r].isalpha():
            ret.append(file[r])
            r+=1
        l=r
        while r<len(file) and file[r].isnumeric():
            r+=1
        if file[l:r]:
            ret.append(file[l:r])
        l=r
    return ret

def diff(l, r):
    l = strsplit(l)
    r = strsplit(r)
    i = 0
    
    while i < min(len(l), len(r)):
        if l[i] == r[i]:
            i += 1
            continue
        if l[i].isnumeric() and r[i].isalpha():
            return -1
        elif l[i].isalpha() and r[i].isnumeric():
            return 1
        elif l[i].isalpha() and r[i].isalpha():
            if l[i].lower() == r[i].lower():
                # l[i] < r[i]
                if l[i].isupper() and r[i].islower():
                    return -1
                else:
                    return 1
            if l[i].lower() < r[i].lower():
                return -1
            else:
                return 1
        elif l[i].isnumeric() and r[i].isnumeric():
            if int(l[i]) == int(r[i]):
                # 이부분 틀렸었고
                cntzl = len(l[i])-len(l[i].lstrip('0'))
                cntzr = len(r[i])-len(r[i].lstrip('0'))
                if cntzl < cntzr:
                    return -1
                else:
                    return 1
            else:
                if int(l[i]) < int(r[i]):
                    return -1
                else:
                    return 1
        i += 1
    return -1 if len(l) < len(r) else 1

files.sort(key=cmp_to_key(diff))
for file in files:
    print(file)
