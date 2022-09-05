class Weird():

    def __init__(self, num1 = 0, num2 = 0):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        text  = str(self.num1) + " "
        text += "# "
        text += str(self.num2) + "$"

        return text

    def Add(self, object):
        if isinstance(object, Weird):
            self.num1 = self.num1 * object.num2
            self.num2 = self.num2 * object.num1


def main():
    c1 = Weird(2, 3)
    print(c1) ##shows 2 # 3$
    c2 = Weird(-4, 7)
    print(c2) ##shows -4 # 7$
    c1.Add(c2)
    print(c1) ##shows 14 # -12$


main()