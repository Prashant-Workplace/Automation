# print("start")
# try:
#     print(x)
# except:
#     print("exception occured")
# print("stop")

# print("start")
# try:
#     print(10/2)
# except:
#     print("exception occured")
# print("stop")

# print("start")
# try:
#     print(10/0)
# except:
#     print("exception occurred and handled")
# else:
#     print("exception not occurred")
# finally:
#     print("this will print if exception occurred or not occurred")
# print("stop")

def age(num):
    if num<1:
        raise ValueError ("age can not be zero or negative")
    if num%2==0:
        print("even")
    else:
        print("odd")

print("calling function to check if number is even or odd")

num=5

try:
    age(num)
except:
    print("exception")

print("program completed")
