#817. Linked List Components
#linked list with all the opeartions



class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp:
            while temp:
                print(temp.data,end="-->")

                temp=temp.next

        else:
            print("the linked list is empty")

    def insert_beginnig(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        Linkedlist.display(self)

    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        Linkedlist.display(self)

    def insert_pos(self,data,pos):
        temp = self.head
        np = Node(data)
        for i in range(pos - 1):
            temp = temp.next
        np.next = temp.next
        temp.next = np
        Linkedlist.display(self)

    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        while temp:
            prev=prev.next
            temp=temp.next
        prev.next=temp.next


l=Linkedlist()
while True:
    print("\n")
    print("1, insert at begnning  2, insert at position  3, insert at end")
    print("7, remove at begnning  8, remove at position  3, remove at end")
    print("5 to display the list")
    n=int(input("enter the value"))
    if n==1:
        data=int(input("enter the data to insert"))
        l.insert_beginnig(data)
    if n==2:
        data = int(input("enter the data to insert"))
        pos=int(input("enter the position"))
        l.insert_pos(data,pos)
    if n==3:
        data = int(input("enter the data to insert"))
        l.insert_end(data)
    if n==5:
        l.display()
    if n==7:
        l.delete_beginning()
    if n==9:
        l.delete_end()
    if n==8:
        pos=int(input("enter the pos"))
        l.delete_pos(pos)

