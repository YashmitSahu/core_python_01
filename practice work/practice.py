class Circle(Shape):
    def execute(self):
        if self.validate():
            self.area()
        else:
            print('Validation Failed')

    def validate(self):
        return False

    def area(self):#
        print('shape area method')


# Rectangle class
class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def validate(self):
        if self.length > 0 and self.width > 0 :
            return True