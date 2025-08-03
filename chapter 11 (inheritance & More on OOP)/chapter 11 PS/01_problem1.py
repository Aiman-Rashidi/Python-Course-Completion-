class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Vector is ({self.i}i + {self.j}j)")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        
    def show(self):
        print(f"Vector is ({self.i}i + {self.j}j + {self.k}k)")

vector_2D = TwoDVector(3, 4)
vector_2D.show()

vector_3D = ThreeDVector(3, 5, 7)
vector_3D.show()