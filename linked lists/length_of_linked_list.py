class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # iterative method of finding length of linked list
    def length_of_list(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    # recursive method for length of the list 
    def length_of_list_recursively(self, node):
        if node is None:
            return 0
        return 1 + self.length_of_list_recursively(node.next)

lnk = LinkedList()
lnk.append('A')
lnk.append('B')
lnk.append('C')
lnk.append('D')
lnk.append('E')
lnk.append('F')

lnk.print_list()
print('\nlength of list: {}'.format(lnk.length_of_list()))
print('\nlength of list recusively: {}'.format(lnk.length_of_list_recursively(lnk.head)))
