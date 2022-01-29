#19. Remove Nth Node From End of List
#take position and remove the corresponding node


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
            print("the list is empty")


    def delete_pos(self,pos):
        previous=self.head
        temp=self.head.next
        for i in range(pos-1):
            previous=previous.next
            temp=temp.next
        previous.next=temp.next


l=LinkedList()
n=Node(1)
l.head=n
n1=Node(2)
l.head.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
n4=Node(5)
n3.next=n4

#Remove the element 3
l.delete_pos(3)

l.display()



