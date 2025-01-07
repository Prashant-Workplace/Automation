import Module1
import Module2

# obj1=Module1.Animal()
# obj1.display()
# obj2=Module2.Bird()
# obj2.display()

from Module1 import Animal
from Module2 import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()