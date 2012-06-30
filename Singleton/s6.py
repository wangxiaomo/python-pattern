#-*- coding: utf-8 -*-

class SingletonMetaClass(type):
    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        original_new = cls.__new__ 

        def my_new(cls, *args, **kw):
            if cls.instance == None:
                cls.instance = original_new(cls, *args, **kw)
            return cls.instance
        cls.instance = None
        cls.__new__ = staticmethod(my_new)

class Bar(object):
    __metaclass__ = SingletonMetaClass
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)


if __name__ == '__main__':
    x = Bar(3)
    print x
    y = Bar(4)
    print y
    z = Bar(5)
    print z


    print x
    print y
    print z
