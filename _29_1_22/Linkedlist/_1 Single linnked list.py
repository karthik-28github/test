#Linked list Single linked list

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
            temp=self.head.next

l=Linked()
n=Node(10)
l.head=n
n1=Node(20)
l.head.next=n1
n2=Node(35)
l.head.next=n2

l.display()

