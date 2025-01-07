# class A:
#     def fun1(self):
#         print("this is class A")
# class B(A):
#     def fun2(self):
#         print("this is class B")
# objA=A()
# objB=B()
# objB.fun2()
# objB.fun1()
from enum import nonmember
from sys import set_coroutine_origin_tracking_depth


# class A:
#     x,y=10,20
#     def fun1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=20,10
#     def fun2(self):
#         print(self.a-self.b)
# objB=B()
# objB.fun1()
# objB.fun2()

# class A:
#     x,y=10,20
#     def fun1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=30,40
#     def fun2(self):
#         print(self.a-self.b)
# class C(B):
#     c,d=70,60
#     def fun3(self):
#         print(self.c*self.d)
# objc=C()
# objc.fun1()
# objc.fun2()
# objc.fun3()

# class A:
#     x,y=10,20
#     def fun1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=30,40
#     def fun2(self):
#         print(self.a-self.b)
# class C(A):
#     c,d=70,60
#     def fun3(self):
#         print(self.c*self.d)
# objb=B()
# objb.fun1()
# objb.fun2()
# objc=C()
# objc.fun1()
# objc.fun3()

# class A:
#     x,y=10,20
#     def fun1(self):
#         print(self.x+self.y)
# class B:
#     a,b=30,40
#     def fun2(self):
#         print(self.a-self.b)
# class C(A,B):
#     c,d=70,60
#     def fun3(self):
#         print(self.c*self.d)
# objc=C()
# objc.fun1()
# objc.fun2()

# class A:
#    def m1(self):
#         print("m1 from class A")
# class B(A):
#     def m1(self):
#         print("m2 from class B")
#         super().m1()
# objb=B()
# objb.m1()

# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# objb=B()
# objb.m1(1000,2000)

# class Parent:
#     var="john"
# class Child(Parent):
#     var="scot"
# obj1=Child()
# print(obj1.var)

# class Bank():
#     def interest(self):
#         return 0
# class XBank(Bank):
#     def interest(self):
#         return "10%"
# class YBank(Bank):
#     def interest(self):
#         return "20%"
# objx=XBank()
# print(objx.interest())
# objy=YBank()
# print(objy.interest())

# class Human():
#     def person(self,name="none"):
#         if name != "none":
#             print("hello " + name)
#         else:
#             print("hello")
# person1=Human()
# person1.person()
# person1.person("scott")

class Calc():
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
obj1=Calc()
obj1.add()
obj1.add(10,20)
obj1.add(100,200,300)