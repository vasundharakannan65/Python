class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def area(self):
        return self.length*self.width
obj= Rectangle(5,4)
print(obj.area())
