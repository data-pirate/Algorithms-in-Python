# In binary search the list to be passed must be sorted else this will not work

#   <================================ BINARY SEARCH ===========================>

position = -1 # initially assuming the value does not exist in the list.

# defining a function for binary search

def binary_search(list, search):
    lower = 0
    upper = len(list)-1

    i = 0

    while lower < len(list):
        mid = (lower + upper) // 2

        if list[mid] == search:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < search:
                lower = mid + 1
            else:
                upper = mid -1
        i +=1
    return False

my_list = [1,2,3,4,5,6,7,8,9]

search = 7

if binary_search(my_list, search):
    print('Element found at {}'.format(position+1))
else:
    print('Oops, the element isn\'t there !')

