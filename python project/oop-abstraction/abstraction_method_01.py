from abc import ABC, abstractmethod


class Shape(ABC):

    def execute(self):
        self.area()

    @abstractmethod
    def area(self):
        pass


class Reactangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        reactangle_area  = self.length * self.width
        print("Rectangle area :",reactangle_area)
        return reactangle_area

#
# # Example usage
r= Reactangle(5,10)
r.execute()
# # Polymorphism: Shape type refrence holding reactangle object
# shape: shape = Reactangle (r,10)
# shape.execute()


