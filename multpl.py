class Felix:
    def felixmethod(self):
        print("This is from Felix Class")

class FelixIts:
    def felixItsmethod(self):
        print("This is from Felix ITs Class")

class FelixItSystem(Felix,FelixIts):
    def FelixItSystemMethod(self):
        print("This is from Felix ITs System")

f=FelixItSystem()
f.felixmethod()
f.felixItsmethod()
f.FelixItSystemMethod()