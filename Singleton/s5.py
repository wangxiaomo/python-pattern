#-*- coding: utf-8 -*-

class SingletonDecorator:
    def __init__(self, kclass):
        self.klass = kclass
        self.instance = None
    def __call__(self, *args, **kw):
        if self.instance == None:
            self.instance = self.klass(*args, **kw)
        return self.instance


@SingletonDecorator
class foo:
    def __str__(self):
        return str(self.val)


if __name__ == '__main__':
    x = foo()
    y = foo()
    z = foo()

    x.val = 3
    y.val = 4
    z.val = 5

    print x
    print y
    print z
