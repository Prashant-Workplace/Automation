# def fun1(i,j):
#     print(i,j)
# fun1(40,20)

# def fun1(i,j=10):
#     print(i,j)
# fun1(0.2)
# fun1(100,300)
# fun1(j=30,i=50)

# def fun1(a,b,c):
#     print(a,b,c)
# fun1(10,20,30)
# fun1(10,20,c=30)
# fun1(10,b=20,c=30)
# #fun1(10,b=20,30)    # positional argument must be always before keyword argument
# #fun1(10,20,b=20)    # this is syntax wise correct but logically wrong. position argument is already assigned to b so again keyword argument can not be assigned to b

def fun1(a,b):
    if a>b:
        print(a,b)
    else:
        print(b,a)
fun1(200,300)