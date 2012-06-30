#-*- coding: utf-8 -*-

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg
    def __str__(self): return str(self.val)


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
