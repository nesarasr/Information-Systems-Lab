class rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        A=self.x * self.y
        print(A)
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

class square:
    def __init__(self,x):
        self.x = x
    def area(self):
        A=self.x * self.x
        print(A)
        return self.x * self.x
    def perimeter(self):
        return 2 * self.x + 2 * self.x
class sphere:
    def __init__(self,x):
        self.x = x
    def area(self):
        A=4*3.14*self.x * self.x
        print(A)
        return 4*3.14*self.x * self.x
    def volume(self):
        return 4*3.14*self.x * self.x*self.x/3
class cube:
    def __init__(self,x):
        self.x = x
    def area(self):
        A=6*self.x * self.x
        print(A)
        return 6*self.x * self.x
    def volume(self):
        return self.x * self.x*self.x
