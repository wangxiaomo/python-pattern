#-*- coding: utf-8 -*-

from __future__ import generators
import random

class Shape(object):
    def factory(type):
        if type == 'Circle': return Circle()
        if type == 'Square': return Square()
        assert 0, "Bad shap creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print "Circle draw"
    def erase(self): print "Circlr erase"


class Square(Shape):
    def draw(self): print "Square draw"
    def erase(self): print "Square erase"

def shape_name_gen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ Shape.factory(i) for i in shape_name_gen(7)]
for shape in shapes:
    shape.draw()
    shape.erase()
