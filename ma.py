class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Parent(object):

    def __init__(self,_i=0):
        self.i=_i

        
    def isFirst(self):
        return self.first

    def fnc(self, arg1, arg2):
            return (arg1*arg2*self.i)
    
    def __getisSecond(self): 
        return self.second

    def __setisSecond(self, value):
        if not(value == 0 or value == 1):
            raise AttributeError
        self.second = value              

    isSecond = property(__getisSecond, __setisSecond)

class First(Parent):
    first = 1
    second = 0
  

class Second(Parent):
    first = 0
    second = 1


class A(First):
    def __init__(self):
        self.i=3
    def fnc(self,value):
            if (value == 7): raise MyError('Error text')
            return super(A,self).fnc(value,value)
