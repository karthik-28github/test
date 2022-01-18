#linked list

class Node:
    def _init_(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None

    def insert_node(self, value):
        if (self.start == None):
            self.start = Node(value)
            self.current = self.start
        else:
            self.current = self.start
            while (self.current.next != None):
                self.current = self.current.next
            self.current.next = Node(value)

    def print_list(self):
        self.current = self.start
        while (self.current != None):
            print(self.current.data, " -> ", end="")
            self.current = self.current.next
        print("None")


L = LinkedList()
while (True):
    ch = int(input("Enter 1 to insert node, 2 to display list, 3 to exit"))
    if (ch == 3):
        break
    elif (ch == 1):
        val = int(input("Enter value to insert : "))
        L.insert_node(val)
    elif (ch == 2):
        L.print_list()
