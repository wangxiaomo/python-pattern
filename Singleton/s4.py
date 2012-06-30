#-*- coding: utf-8 -*-

class Singleton(object):
    __instance = None
    def __new__(cls, val):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance
    def __str__(self):
        return str(self.val)


if __name__ == '__main__':
    x = Singleton(3)
    print x
    y = Singleton(4)
    print y
    z = Singleton(5)
    print z 
    
    print x
    print y
    print z
