import sys

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

def main():
    for i in range(len(knapsack)):
        for j in range(len(knapsack[0])):
            if j < stuff[i][0]:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                knapsack[i][j] = max(
                    stuff[i][1] + knapsack[i - 1][j - stuff[i][0]], knapsack[i - 1][j]
                )
    print(knapsack[-1][-1])
    return


if __name__ == "__main__":
    main()
