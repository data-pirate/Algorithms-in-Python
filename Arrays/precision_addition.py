def plus(A, to_add):
    A[-1] += to_add
    for i in reversed(range(1, len(A))):
        if A[i] <= 10 :
            break
        temp = A[i]
        A[i] = A[i] % 10
        A[i-1] += int(temp / 10)
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


A1 = [2, 4, 1]
print(plus(A1, 20))
# will print [2, 6, 1]
