# x=int(input("enter the value of a "))
# try:
#     result =10/x
#     print(result)
# except ZeroDivisionError as error:
#         print("it is not possible ")
# finally: #it will print as it is in the end
#     print("i will be executed anyhow ")\

# x=int(input("enter the value of a "))
# try:
#     result =10/2
#     print(result)
# except NameError as error:
#       print("its okay its a aline change ")
# finally:
#     print("it works ")

try:
    a=4
    b=2
    result=a/b
except Exception as error:
    print("please u cannot divide by 0")
else:
    if a%b==0:
        print("it is even number ")
finally:
    print(result)