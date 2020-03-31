# Array1 = [1, 4, 9] + 1 will result in [1, 5, 0]
# Array2 = [9, 9, 9] + 1 will result in [1, 0, 0, 0]

def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i-1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


arr = [1,4,9]
print(plus_one(arr))
# prints [1, 5, 0]

arr = [9, 9, 9]
print(plus_one(arr))
# prints [1, 0, 0, 0]
