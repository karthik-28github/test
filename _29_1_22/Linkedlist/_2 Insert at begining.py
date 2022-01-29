#Insertion at the begining of the list


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked():
    def __init__(self):
        self.head=None

    def display(self):
        if self.head==None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp:
                    print(temp.data,"---->",end=" ")
                    temp=temp.next
    def insert_begning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb




l=Linked()
n=Node(10)
l.head=n
n1=Node(20)
l.head.next=n1

l.insert_begning(5)
l.insert_begning(3)

l.display()
