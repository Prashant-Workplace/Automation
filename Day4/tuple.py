# tuple1=("apple","banana","cherry")
# print(tuple1)

# tuple1=("apple","banana","cherry")
# print(tuple1[-3])
# print(tuple1[1])
#
# tuple1=("apple","banana","cherry","orange","kiwi","mealon","mangos")
# print(tuple1[2:5])
# print(tuple1[-4:-1])

# tuple1=("apple","100","cherry")
# list1=list(tuple1)
# list1[0]="orange"
# print(list1)
# tuple1=tuple(list1)
# print(tuple1)

# tuple1=("apple",100,"cherry")
# for i in tuple1:
#     print(i)

# tuple1=("apple",100,"cherry")
# if "cherry" in tuple1:
#     print("item present")
# else:
#     print("item absent")

# tuple1=("apple",100,"cherry")
# print(len(tuple1))

# tuple1=("apple",100,"cherry")
# tuple1[0]="orange"
# print(tuple1)

# tuple1=("apple",100,"cherry")
# tuple2=tuple1
# print(tuple2)

# tuple1=("apple",100,"cherry")
# del tuple1
# print(tuple1)

# tuple1=("apple","mango","cherry")
# tuple2=(10,20,30)
# tuple3=tuple1+tuple2
# print(tuple3)

tuple1=("apple",100,"cherry")
tuple2=(10,20,30)
tuple3=(10,20,30)
if tuple1==tuple2:
    print("1 and 2 equal")
elif tuple2==tuple3:
    print("2 and 3 equal")
else:
    print("not equal")