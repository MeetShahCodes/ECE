import time
import matplotlib
import matplotlib.pyplot as plt

count = 0
countDict = 0

def fib(n):
    global count
    count += 1
    if(n==1 or n==2):
        return 1
    return fib(n-1) + fib(n-2)

def fibDict(n, dict={1:1, 2:1}):
    global countDict
    countDict+=1
    try:
        return dict[n]
    except:
        dict[n] = fibDict(n-1, dict)+fibDict(n-2, dict)
        return dict[n]

def getTime(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end-start

x = [i for i in range(1, 33)]
y = [getTime(fib, i) for i in x]
z = [getTime(fibDict, i) for i in x]

plt.plot(x, y)
plt.plot(x, z)
plt.show()

class Shapes:
    def __init__(self, name):
        self.name = name
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
class Circle:
    def __init__(self, r):
        super().__init__("circle")
        self.r = r
    def get_area(self):
        return 3.14*(self.r**2)
    def get_perimeter(self):
        return 2*3.14*self.r
class Square:
    def __init__(self, a):
        super().__init__("square")
        self.a = a
    def get_area(self):
        return self.a**2
    def get_perimeter(self):
        return 4*self.a
class Rectangle:
    def __init__(self, a, b):
        super().__init__("rectangle")
        self.a = a
        self.b = b
    def get_area(self):
        return self.a*self.b
    def get_perimeter(self):
        return 2*(self.a+self.b)
class Triangle:
    def __init__(self, a, b, c):
        super().__init__("triangle")
        self.a = a
        self.b = b
        self.c = c
    def get_area(self):
        a, b, c = self.a, self.b, self.c
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**(0.5)
    def get_perimeter(self):
        return self.a+self.b+self.c

shapeName = input("Enter shape name: ")
shape = None

if shapeName=="circle":
    r = input("Enter radius: ")
    shape = Circle(r)
elif shapeName=="square":
    a = input("Enter side length: ")
    shape = Square(a)
elif shapeName=="rectangle":
    a = input("Enter side a: ")
    b = input("Enter side b: ")
    shape = Rectangle(a, b)
elif shapeName=="triangle":
    a = input("Enter side a: ")
    b = input("Enter side b: ")
    c = input("Enter side c: ")
    shape = Triangle(a, b, c)
else:
    print("Invalid name")

print(shape.get_area())
print(shape.get_perimeter())
    

