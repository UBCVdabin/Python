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