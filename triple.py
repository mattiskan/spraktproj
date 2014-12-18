#!/usr/bin/python3

class Triple:
    def __init__(self, A, R, B):
        self.__A = A
        self.__R = R
        self.__B = B
   
    def A(self):
        return self.__A

    def R(self):
        return self.__R

    def B(self):
        return self.__B

    def __eq__(self, other):
        return (self.__A == other.__A and
                self.__R == other.__R and
                self.__B == other.__B)
    def __str__(self):
        return str(self.__A) + str(self.__R) + str(self.__B)

