from Basic.shape import Shape


class Rectangle(Shape):

    def __init__(self):
        super().__init__()

        self.height = None
        self.width = 0

    def set_height(self,height):
        self.height = height

    def set_width(self,width):
        self.width = width

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

shape = Rectangle()
shape.set_height(10)
shape.set_width(8)
print("width",shape.get_width())
print("height ", shape.get_height())



