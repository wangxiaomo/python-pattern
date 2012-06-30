#-*- coding: utf-8 -*-

class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return `self` + str(self.val)

    instance = None
    def __new__(cls):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name ,value):
        return setattr(self.instance, name, value)


if __name__ == '__main__':
    x = OnlyOne()
    x.val = 3
    print x
    y = OnlyOne()
    y.val = 4
    print y
    z = OnlyOne()
    z.val = 5
    print z

    print x
    print y
    print z
