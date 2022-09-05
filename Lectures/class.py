class Rectangle():
    def __init__(self, w = 1, h = 2):
        self.width = w
        self.height = h

    def __str__(self):
        s = "Width = " + str(self.width) + ", Height = " + str(self.height)
        p = self.getPerimeter()
        s += (", Perimeter = " + str(p))
        return s

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return 2 * (self.height + self.width)

r = Rectangle()
print(r)
print(r.getPerimeter)
print(r.getPerimeter())
print(r.getArea)
print(r.getArea(), end ="\n\n")

r = Rectangle(10, 20)
print(r)
print(r.getPerimeter)
print(r.getPerimeter())
print(r.getArea)
print(r.getArea())

# Human Class 생성 및 활용 (기본)
#region

class Human():

    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def Eat(self, amount):
        self.weight += amount
        self.height += 0.5

    def __str__(self):
        s = "Weight = " + str(self.weight) + ", Height = " + str(self.height)
        return s

    def Exercise(self):
        self.weight -= 1
        self.height += 0.5

#amy = Human(15, 1.3)
#bob = Human(5, 0.9)
#asdf = Human()

#bob.Eat(10)
#print(bob)

#endregion