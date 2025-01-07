# dic1={101:"X",102:"Y",103:"Z"}
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# print(dic1["brand"])
# print(dic1["model"])
# print(dic1.get("year"))
# print(dic1)
# dic1["year"]=2022
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# for i in dic1:
#     print(dic1[i])
# for i in dic1.values():
#     print(i)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# for (x,y) in dic1.items():
#     print(x,y)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# if "model" in dic1:
#     print("exists")
# else:
#     print("not exists")
# print(len(dic1))

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# dic1 ["color"]="red"
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# dic1.pop("year")
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# del dic1["year"]
# print(dic1)
#
# del dic1
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# dic1.clear()
# print(dic1)

# dic1={
#     "brand":"hyundai",
#     "model":"i10",
#     "year":2021
# }
# dic2=dic1
# print(dic2)
# print(dic1)

dic1={
    "brand":"hyundai",
    "model":"i10",
    "year":2021
}
dic2=dic1.copy()
print(dic2)