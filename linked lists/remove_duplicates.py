class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node = None
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dups = dict()        
        while cur:
            if cur.data in dups:
                prev.next = cur.next
                cur = None
            else:
                dups[cur.data] = 1
                prev = cur
            cur = prev.next
llist = LinkedList()

llist.append(2)
llist.append(3)
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(8)
llist.append(8)
llist.append(8)
llist.append(8)

print('\noriginal linked list:\n')
llist.printlist()

llist.remove_duplicates()
print('\nlinked list after duplicates are removed:\n')
llist.printlist()
