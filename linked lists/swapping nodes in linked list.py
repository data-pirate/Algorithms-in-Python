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

    # swapping two Nodes 
    def node_swap(self, key1, key2):
        if key1 == key2:
            return
        
        prev_of_1 = None
        cur_of_1 = self.head
        while cur_of_1 and cur_of_1.data != key1:
            prev_of_1 = cur_of_1
            cur_of_1 = cur_of_1.next

        prev_of_2 = None
        cur_of_2 = self.head
        while cur_of_2 and cur_of_2.data != key2:
            prev_of_2 = cur_of_2
            cur_of_2 = cur_of_2.next

        if prev_of_1:
            prev_of_1.next = cur_of_2
        else:
            self.head = cur_of_2

        if prev_of_2:
            prev_of_2.next = cur_of_1
        else:
            self.head = cur_of_1

        cur_of_1.next, cur_of_2.next = cur_of_2.next, cur_of_1.next


lnk = LinkedList()
lnk.append('A')
lnk.append('B')
lnk.append('C')
lnk.append('D')
lnk.append('E')
lnk.node_swap('B', 'C')


lnk.print_list()
print('\nlength of list: {}'.format(lnk.length_of_list()))
print('\nlength of list recusively: {}'.format(lnk.length_of_list_recursively(lnk.head)))
