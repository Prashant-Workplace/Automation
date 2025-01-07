import sys
sys.path.append ("//Day9/PackA")
sys.path.append ("//Day9/PackB")

from emp import Employee
from stu import Student

obj1=Employee(101,"john",500000)
obj1.displayemp()

obj2=Student(102,"scott","A")
obj2.displaystu()