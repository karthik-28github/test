'''
You are given four points  and  in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points  and  in degrees(not radians). Let the angle be .

 where  x  and  x .

Here,  means the dot product of  and , and  x  means the cross product of vectors  and . Also, .

Input Format

One line of input containing the space separated floating number values of the  and  coordinates of a point.

Output Format

Output the angle correct up to two decimal places.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2
Sample Output

8.19
'''
import math


class Points(object):
    # Class 2 - Find the Torsional Angle in Python - HackerRank Solution START
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    # Class 2 - Find the Torsional Angle in Python - HackerRank Solution END

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))