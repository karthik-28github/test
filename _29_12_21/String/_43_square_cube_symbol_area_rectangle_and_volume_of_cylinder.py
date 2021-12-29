# class Rectangle:
#     def area_rectangle(self,length,width):
#         Area=length*width
#         print(f'area of rectangle is:{Area}')
# l=int(input("enter length of rectangle:"))
# w=int(input("enter width of rectangle:"))
# r1=Rectangle()
# r1.area_rectangle(l,w)
print("--------------------")
# class Cylinder:
#     def volume_cylinder(self,radius,height):
#         volume=3.14*radius*radius*height
#         print(f'Volume of cylinder is:{volume}')
#
# r=int(input("enter radius is cylinder:"))
# h=int(input("enter height of cylinder:"))
# c1=Cylinder()
# c1.volume_cylinder(r,h)

print("----------------")
class Number:
    def __init__(self,num):
        self.num=num
    def square(self):
        res=self.num*self.num
        print(f'square of a number is:{res}')

    def cube(self):
        res1 = self.num * self.num * self.num
        print(f'cube of a number is::{res1}')

num=int(input("enter a number:"))
n1=Number(num)
n1.square()
n1.cube()
