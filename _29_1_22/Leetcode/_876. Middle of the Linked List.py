#876. Middle of the Linked List


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if self.head:
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
        else:
            print("the linked list is empty")

    def insert_pos(self,data,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nb=Node(data)
        nb.next=temp.next
        temp.next=nb




l=LinkedList()
n=Node(0)
l.head=n
n1=Node(2)
l.head.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
n4=Node(5)
n3.next=n4

l.display()
print("\n")

l.insert_pos(1,1)
l.display()