import sys
input = sys.stdin.readline
# 상대방의 체력을 정확하게 0으로 만들면서 마나 포인트를 최대한 적게 사용하는 것이다. 
# 과연 광현이는 이 제약을 지킬 수 있을까? 광현이의 플레이가 맞는지 확인하기 위해 
# 적의 체력을 정확하게 0으로 만들 때 필요한 가장 적은 마나 포인트를 구해보자.
# input은 몽땅 <=100
N,M,K = map(int,input().split())
# M,K = hp, mana increment

manacosts_damage = []
maxdmg = 0
for _ in range(N):
    X,Y = map(int,input().split())
    # X,Y = mana cost, damage
    maxdmg = max(maxdmg,Y)
    manacosts_damage.append([X,Y])
hp = [[[M-i,100001],[0 for _ in range(N)]] for i in range(M+1)]
for i in range(len(manacosts_damage)):
    hp[0][1][i]=manacosts_damage[i][0]
hp[0][0][1]=0 
print(hp)
for i in range(len(hp)):
    print(hp[i])
    for idx, ccost in enumerate(hp[i][1]):
        dmg = manacosts_damage[idx][1]
        if i+dmg >= len(hp):
            continue
        if hp[i+dmg][0][1] > hp[i][0][1]+ccost:
            hp[i+dmg][0][1] = hp[i][0][1]+ccost
            hp[i+dmg][1] = hp[i][1][::]
            hp[i+dmg][1][idx]+=K
print(hp[-1][0][1])
