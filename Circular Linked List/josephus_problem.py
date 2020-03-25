# There are n people standing in a circle waiting to be executed.
# The counting out begins at some point in the circle and proceeds
# around the circle in a fixed direction. In each step, a certain
# number of people are skipped and the next person is executed. 
# The elimination proceeds around the circle (which is becoming smaller
# and smaller as the executed people are removed), until only the last 
# person remains, who is given freedom. Given the total number of persons
# n and a number k which indicates that k-1 persons are skipped and kth 
# person is killed in circle. The task is to choose the place in the initial 
# circle so that you are the last one remaining and so survive.


class Node:
    def __init__(self, data):
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
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head:
            cur = self.head
            if cur and cur.data == key:
                while cur.next != self.head:
                    cur = cur.next
                self.head = self.head.next
                cur.next = self.head
            else:
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next
                        return

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove_node(self, node):
        if self.head:
            cur = self.head
            if cur == node:
                while cur.next != self.head:
                    cur = cur.next
                self.head = self.head.next
                cur.next = self.head
            else:
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur == node:
                        prev.next = cur.next
                        cur = cur.next

    # here is the implementation
    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            
            print('KILL:' + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.print_list()
cllist.josephus_circle(2)
cllist.print_list()
