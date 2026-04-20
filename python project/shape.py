class Shape:
    def __init__(self):
        self.colour = None
        self.border = 0

    def set_colour(self, colour):
        self.colour = colour

    def set_border(self, border):
        self.border = border

    def get_border(self):
        return self.border
    def get_colour(self):
        return self.colour

sp = Shape()
sp.set_border(1)
sp.set_colour("red")
print(sp.get_colour())
print(sp.get_border())