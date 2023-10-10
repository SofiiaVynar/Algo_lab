def max_min_distance(N, C, stalls):
    if 2 <= N <= 100000 and 2 <= C <= N:
        stalls.sort()
        low = 0
        high = stalls[-1] - stalls[0]
        result = 0
        find_stalls = []

        while low <= high:
            mid = (low + high) // 2
            cow_placed = 1
            prev_stall = stalls[0]
            needed_stalls = [stalls[0]]

            for stall in stalls:
                if stall - prev_stall >= mid:
                    cow_placed += 1
                    prev_stall = stall
                    needed_stalls.append(stall)

            if cow_placed < C:
                high = mid - 1
            else:
                result = mid
                find_stalls = needed_stalls
                low = mid + 1

        return result, find_stalls
    else:
        print("Error")


N = 5
C = 3
stalls = [1, 2, 3, 4, 5, 10, 30, 40, 60, 90]
result = max_min_distance(N, C, stalls)
print(result)
