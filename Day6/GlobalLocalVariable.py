# gv=100
# def fun1():
#     lv=200
#     print(lv)
# fun1()

# gv=100
# def fun1():
#     lv=200
#     print(lv)
#     print(gv)
# fun1()

# gv=100
# def fun1():
#     gv=200
#     print(gv)
# fun1()
# print(gv)

# gv=100
# def fun1():
#     global gv
#     gv=200
#     print(gv)
# fun1()
# print(gv)

def fun1():
    global gv
    gv=200
    print(gv)
fun1()
print(gv)