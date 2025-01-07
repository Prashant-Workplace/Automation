# class Class1:
#     def fun1(self,a):
#         print(a)
# obj1=Class1()
# obj1.fun1("this is my first class and methods creation program")
from encodings.punycode import punycode_encode


# class Class1:
#     @staticmethod
#     def fun1(self,a):
#         print(self,a)
# #obj1=Class1()
# #obj1.fun1("static method","this is my first class and methods creation program")
# Class1.fun1(1,2)

# class Class1:
#     a=10,b=20
#       def fun1(self):
#         print(self.a+self.b)
# obj1=Class1()
# obj1.fun1()

# i,j=1,2
# class Class1:
#     a,b=10,20
#     def fun1(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# obj1=Class1()
# obj1.fun1(100,200)

# a,b=1,2
# class Class1:
#     a,b=10,20
#     def fun1(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()["a"]+globals()["b"])
# obj1=Class1()
# obj1.fun1(100,200)

# class Class1:
#     a,b=10,20
#     def fun1(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()["a"]+globals()["b"])
# obj1=Class1()
# obj1.fun1(100,200)

# class Class1:
#     def __init__(self):
#         print("this is constructor")
#     def fun1(self):
#         print("this is method")
# obj1=Class1()
# obj1.fun1()

class Class1:
    place="pune"
    def __init__(self,place):
        print(place)
        print(self.place)

obj1=Class1("paris")
