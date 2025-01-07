import sys

from Day9.Pack1.Module3 import display

sys.path.append ("//Day9/Package1")
sys.path.append ("//Day9/Package1/Package2")

# import Module3
# import Module4
#
# # Module3.display()
# # Module4.show()

from Module3 import *
from Module4 import *

display()
show()