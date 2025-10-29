class Shape:
    def __init__(self,sides):
        self.sides = sides
    def no_of_sides(self):
        print(self.sides)        

class Color:
    def __init__(self,col):
        self.col = col

class Square(Shape,Color):
    def __init__(self,sides,col):
        Shape.__init__(self,sides)
        Color.__init__(self,col)
    def no_of_sides(self):
        print(4)
sq = Square(5,"Green")
Sh = Shape(3)
for i in (sq,Sh):
    i.no_of_sides()
        