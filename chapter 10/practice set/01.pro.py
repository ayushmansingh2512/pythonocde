class TwoDVector:
    def __init__(self , i , j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i} + {self.j}")

class ThreeDVector(TwoDVector):
    def __init__(self , i , j , k):
        super().__init__(i,j)
        self.k= k
    
    def show(self):
        print(f"The vector is {self.i} + {self.j} + {self.k}")
    
a = TwoDVector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()