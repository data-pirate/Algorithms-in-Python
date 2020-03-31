def array_advance_array(arr):
    farthest_reached = 0
    size = len(arr) - 1
    counter = 0
    while counter <= farthest_reached and farthest_reached < size:
        farthest_reached = max(farthest_reached, arr[counter] + counter)
        counter += 1
    return farthest_reached == size

A = [2, 3, 1, 0, 2, 0, 1]
print(array_advance_array(A))
# prints True

A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance_array(A))
# prints False as its impossible to win situation
