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
