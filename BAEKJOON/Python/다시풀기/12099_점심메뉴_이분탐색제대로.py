def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    index = 2
    
    taste = []
    for _ in range(n):
        first = int(data[index])
        second = int(data[index + 1])
        taste.append((first, second))
        index += 2

    # Sort the list based on the first element of the tuples
    taste.sort()

    # Function to perform lower bound binary search
    def lower_bound(arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid][0] < target:
                low = mid + 1
            else:
                high = mid
        return low

    # Function to perform upper bound binary search
    def upper_bound(arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid][0] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    results = []
    # Handling queries
    for _ in range(q):
        u = int(data[index])
        v = int(data[index + 1])
        x = int(data[index + 2])
        y = int(data[index + 3])
        index += 4
        
        # Finding the relevant range using manual binary search
        start = lower_bound(taste, u)
        end = upper_bound(taste, v)
        
        # Count how many are within the specified range for the second element
        cnt = 0
        for i in range(start, end):
            if x <= taste[i][1] <= y:
                cnt += 1
        
        results.append(cnt)
    
    # Output all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
