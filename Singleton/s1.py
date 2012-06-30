#-*- coding: utf-8 -*-

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return `self` + str(self.val)

    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)


if __name__ == '__main__':
    x = OnlyOne(3)
    print x
    y = OnlyOne(4)
    print y
    z = OnlyOne(5)
    print z

    print x
    print y
    print z
