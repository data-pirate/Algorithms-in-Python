class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            new_node = Node(data)
            while cur.next != self.head:
                cur = cur.next
            
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)     
            cur = cur.next
            if cur == self.head:
                break
    
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        cur = self.head
        if size == 0:
            return None
        if size == 1:
            print(self.head)
        
        mid = size//2
        count = 0

        prev = None
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_list = CircularLinkedList()
        while cur.next != self.head:
            split_list.append(cur.data)
            cur = cur.next
        split_list.append(cur.data)
        self.print_list()
        print('\n')
        split_list.print_list()
    
cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.split_list()
