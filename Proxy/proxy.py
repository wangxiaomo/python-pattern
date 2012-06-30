#-*- coding: utf-8 -*-

class Implementation(object):
    def f(self): print "F"
    def g(self): print "G"
    def h(self): print "H"


class Proxy(object):
    def __init__(self):
        self.__implementation = Implementation()
    def __getattr__(self, name):
        return getattr(self.__implementation, name)


if __name__ == '__main__':
    x = Proxy()
    x.f()
    x.g()
    x.h()
