#


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None

    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next
        else:
            print("the linked list is empty")

    def delete_pos(self,pos):
        previous = self.head
        temp=self.head.next
        for i in range(pos-1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next

l=LinkedList()
n=Node(1)
l.head=n
n2=Node(2)
l.head.next=n2

n3=Node(3)
n2.next=n3

n4=Node(4)
n3.next=n4

n5=Node()
# l.delete_begning()
l.delete_end()

# l.delete_pos(2)
l.display()
