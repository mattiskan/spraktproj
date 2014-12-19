from nltk.stem import WordNetLemmatizer

class Triple:
    wnl = WordNetLemmatizer()

    def __init__(self, A, R, B, Tree):
        self.__A = A
        self.__R = R
        self.__B = B
        #self.__A[0] = Triple.wln.lemmatize(self.__A[0])
        #self.__R[0][0] = Triple.wnl.lemmatize(self.__R[0][0])
        #self.__B[0] = Triple.wln.lemmatize(self.__B[0])
        self.__Tree = Tree

    def A(self):
        return self.__A[0][0]

    def R(self):
        return self.__R[0][0]

    def B(self):
        return self.__B[0][0]

    def ALemma(self):
        return Triple.wln.lemmatize(self.__A[0][0])

    def RLemma(self):
        return Triple.wln.lemmatize(self.__R[0][0])

    def BLemma(self):
        return Triple.wln.lemmatize(self.__B[0][0])

    def Tree(self):
        return self.__Tree

    def drawTree(self):
        self.__Tree.draw()

    def __eq__(self, other):
        return (self.__A == other.__A and
                self.__R == other.__R and
                self.__B == other.__B)

    def __str__(self):
        return "(%s --%s--> %s)" % (self.A(), self.R(), self.B())

