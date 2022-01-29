#Linked list with insertion at all the postion begining end and inbetween the nodes

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None

    def display(self):
        if self.head:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
        else:
            print("the linked list is empty")
    def insert_begning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def insert_pos(self,data,pos):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np


l=LinkedList()

n=Node(3)
l.head=n
n1=Node(4)
l.head.next=n1

l.insert_begning(2)
l.insert_begning(1)

l.insert_end(6)
l.insert_end(7)

l.insert_pos(5,4)

l.display()



