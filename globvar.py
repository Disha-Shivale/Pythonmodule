#Global variable
i = 10
j = 20
def total():
    print(i + j)
total()
print()

#Global keyword
def show():
    global i, j
i,j = 20,20
show()
print(i+j)
print()

