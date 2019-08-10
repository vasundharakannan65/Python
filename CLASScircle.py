class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        pi=3.1415
        return pi*self.radius**2
obj=Circle(5)
print(obj.area())
