def ismixed(arr):
    if arr[0] == 1:
        for i in range(1, 8):
            if arr[i] != i + 1:
                return "mixed"
        else:
            return "ascending"

    elif arr[0] == 8:
        for i in range(1, 8):
            if arr[i] != 8 - i:
                return "mixed"
        else:
            return "descending"

    return "mixed"

arr = list(map(int, input().split()))
print(ismixed(arr))

