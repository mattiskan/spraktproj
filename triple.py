class Triple:
    def __init__(self, A, R, B):
        self.__A = A
        self.__R = R
        self.__B = B
   
    def A(self):
        return self.__A[0][0]

    def R(self):
        return self.__R[0][0]

    def B(self):
        return self.__B[0][0]

    def __eq__(self, other):
        return (self.__A == other.__A and
                self.__R == other.__R and
                self.__B == other.__B)

    def __str__(self):
        return "(%s --%s--> %s)" % (self.A(), self.R(), self.B())

