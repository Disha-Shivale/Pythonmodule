class Felix:
    def felixMethod(self):
        print("This is from felix class")

class FelixITs(Felix):
    def felixItsMethod(self):
        print("This is from Felix ITs Class")

f = FelixITs()
f.felixMethod()
f.felixItsMethod()



