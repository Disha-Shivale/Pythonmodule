class Felix:
    def felixMethod(self):
        print("This is from felix class")

class FelixITs(Felix):
    def felixItsMethod(self):
        print("This is from felix ITs class")

class FelixITsSystem(FelixITs):
    def felixItSystemMethod(self):
        print("This is from Felix ITs System")

f = FelixITsSystem()
f.felixMethod()
f.felixItsMethod()
f.felixItSystemMethod()

