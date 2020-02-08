def anagram(string1, string2):
    clean_string1 = string1.replace(" ", "").lower()
    clean_string2 = string2.replace(" ", "").lower()

    if len(clean_string1) == len(clean_string2):
        if sorted(clean_string1) == sorted(clean_string2):
            return True
    else:
        return False 

x = input('str1: ')
x2 = input('str2: ')

if anagram(x,x2):
    print('true')
else:
    print('false')
