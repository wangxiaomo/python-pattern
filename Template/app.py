#-*- coding: utf-8 -*-

class ApplicationFramework:
    def __init__(self):
        self.__templateMethod()
    def __templateMethod(self):
        for i in range(5):
            self.customize1()
            self.customize2()


class MyApp(ApplicationFramework):
    def customize1(self):
        print "customize1"
    def customize2(self):
        print "customize2"


if __name__ == '__main__':
    MyApp()
