class  Stack():
    def __init__(self):
        self.items = list()

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def convert_int_to_bin(dec_num):
    stk = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        dec_num //= 2
        stk.push(remainder)

    bin_num = ''
    while not stk.is_empty():
        bin_num += str(stk.pop())
    
    return bin_num

print(convert_int_to_bin(65))