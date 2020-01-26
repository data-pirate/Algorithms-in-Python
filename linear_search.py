
# initially assuming that the number does not exists in the list
position = -1 

# defining a function for linear search which accepts twwo arguments list and item to be searched
def linear_search(list, obj):
    for i in range(len(list)):
        if obj == list[i]:
            globals()['position']     = i
            return True
    return False

my_list = [90, 98, 912, 123, 23, 88, 92, 75, 123]

search = 23

if linear_search(my_list, search):
    print('number found at : {}'.format(position))
else:
    print('Not Present in the list !!')

# Output : 
# number found at : 4