# set1={"apple","banana","cherry"}
# print(set1)

# set1={"apple","banana","cherry"}
# for i in set1:
#     print(i)

# set1={"apple","banana","cherry"}
# print("apple" in set1)
# print("orange" in set1)
# set1.add("grapes")
# print(set1)
# set1.update(["lichi","jackfruit"])
# print(set1)
# print(len(set1))

# set1={"apple","banana","cherry"}
# set1.remove("apple")
# print(set1)
# set1.remove("xyz")
# print(set1)

# set1={"apple","banana","cherry"}
# set1.discard("apple")
# print(set1)
# set1.discard("xyz")
# print(set1)

# set1={"apple","banana","cherry"}
# set1.clear()
# print(set1)
# del set1
# print(set1)

set1={"apple","banana","cherry"}
set2={10,20,30,"orange"}
print(set1.union(set2))
set1.update(set2)
print(set1)
