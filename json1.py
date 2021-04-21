import json
person = '{ "name":"john", "email":"john@gmail.com","age":35}'
i = json.loads(person)
print(i["name"] + " " + i["email"] + " ", i["age"])
print()

#Example 2
i = json.loads(person)
print(i)
print()

#Nested Function
def demo1():
    print("Demo 1 method")

    def innerOne():
        print("Inner Method 1")

    def innerTwo():
        print("Inner Method 2")
    innerOne()
    innerTwo()
demo1()
print()

#Nested class
class Demo:
    def method1(self):
        print('This is Demo class Method 1')
class User:
    def method2(self):
        print('This is User class Method 2')
d = Demo()
d.method1()
d1 = User()
d1.method2()







