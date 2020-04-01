A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

def intersection_sorted_array(arr1, arr2):
    i = 0
    j = 0
    intersection = list()
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] != arr1[i-1] or i == 0:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return intersection

print(intersection_sorted_array(A, B))
