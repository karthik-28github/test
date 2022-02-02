#818. Race Car

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist():
    def __init__(self):
        self.head=None

    def add_end(self,data):
        nd=Node(data)
        temp=self.head
        while temp:
            temp=temp.next
        temp.next=nd

    def display(self):
        temp=self.head
        if temp:
            print(temp.data,end="->")
            temp=temp.next
        else:
            print("the linked list is empty")

l=Linkedlist()
start1=Node(0)
l.head=start1
l.display()
start=0
speed=1
target=6
count=0
#A-accelator position=speed  speed=speed*2
#R-reverse    postion-1

str1=""
while(start!=target):
      print(str1)
      print("start", start)
      print("speed", speed)
      if start<target :

          str1=str1+"A"
          start=start+speed
          speed*=2
          print( str1)
          print("start",start)
          print("speed",speed)

      elif start>target:
          str1=str1+"R"
          start=start-1
          speed=1
          print(str1)
          print(start)






