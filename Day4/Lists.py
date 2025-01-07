# list1=[10,20,30,40]
# list2=["apple","banana","cherry"]
# list3=["apple",10,"banana",20]
# print(list1)
# print(list2)
# print(list3)

# list3=["apple",10,"banana",20]
# print(list3[2])
# print(list3[-1])

# list3=["apple",10,"banana",20,"cherry",30]
# print(list3[2:4])
# print(list3[2:-1])

# list3=["apple",10,"banana",20,"cherry",30]
# list3[2]="MANGO"
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# for i in list3:
#     print(i)

# list3=["apple",10,"banana",20,"cherry",30]
# if "cherry" in list3:
#     print("cherry is present")
# else:
#     print("cherry is not present")

# list3=["apple",10,"banana",20,"cherry",30]
# print(len(list3))

# list3=["apple",10,"banana",20,"cherry",30]
# list3.append("orange")
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# list3.insert(1,"orange")
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# list3.pop(1)
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# del list3[3]
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# list3.clear()
# print(list3)

# list3=["apple",10,"banana",20,"cherry",30]
# list4=list(list3)
# print(list3)
# print(list4)

# list3=["apple",10,"banana",20,"cherry",30]
# list4=list3.copy()
# print(list3)
# print(list4)

# list1=["a","b","c"]
# list2=[1,2,3]
# print(list1+list2)

# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)
# print(list2)

# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)

list1=["apple",100,"cherry"]
list2=[10,20,30]
list3=[10,20,30]
if list1==list2:
    print("1 and 2 equal")
elif list2==list3:
    print("2 and 3 equal")
else:
    print("not equal")