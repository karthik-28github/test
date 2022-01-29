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

    def insert_pos(self,data,pos):
        temp=self.head
        np=Node(data)
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np




l=Linked()
n=Node(10)
l.head=n
n1=Node(20)
l.head.next=n1

pos=1
l.insert_pos(11,pos)
l.display()
