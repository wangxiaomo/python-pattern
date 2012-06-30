#-*- coding: utf-8 -*-

class State:
    def __init__(self, imp):
        self.__implementation = imp 
    def changeImp(self, new_imp):
        self.__implementation = new_imp
    def __getattr__(self, name):
        return getattr(self.__implementation, name)



class Imp1:
    def f(self):
        print "F1"
    def g(self):
        print "G1"


class Imp2:
    def f(self):
        print "F2"
    def g(self):
        print "G2"


if __name__ == '__main__':
    b = State(Imp1())
    b.f()
    b.g()
    b.changeImp(Imp2())
    b.f()
    b.g()
