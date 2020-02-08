def hamming_distance(str1, str2):

    if len(str1) != len(str2):
        return None

    hamming_distance = 0

    for index, _ in enumerate(str1):
        if str1[index] != str2[index]:
            hamming_distance += 1

    return hamming_distance


inp = input('enter string: ')
inp2 = input('enter 2nd string: ')

print(hamming_distance(inp, inp2))
