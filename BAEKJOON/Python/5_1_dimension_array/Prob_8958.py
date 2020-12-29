N = int(input())
Array = []
tempArray = []
Point = 0
Score = 0
for i in range(0,N,1):
    Array = input()
    length = len(Array)
    for i in range(0,length,1):
        if (Array[i] == 'O'):
            if (Array[i-1]==Array[i]):
                Point = Point + 1
            else:
                Point = 1
        else:
            Point = 0
        Score = Point + Score
    print(Score)
    Score = 0
    Point = 0
    Array = []
