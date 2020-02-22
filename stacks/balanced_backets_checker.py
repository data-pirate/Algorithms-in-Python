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

def is_match(prn1, prn2):
    if prn1 == '(' and prn2 == ')':
        return True
    elif prn1 == '[' and prn2 == ']':
        return True
    elif prn1 == '{' and prn2 == '}':
        return True
    else:
        return False
    

def is_brackets_balanced(word):
    stk = Stack()
    is_balanced = True
    index = 0

    while index < len(word) and is_balanced:
        bracket = word[index]
        if bracket in '[({':
            stk.push(bracket)
        else:
            if stk.is_empty():
                is_balanced = False
            else:
                top = stk.pop()
                if not is_match(top, bracket):
                    is_balanced = False
        index += 1

    if stk.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_brackets_balanced("((()[]){})"))
