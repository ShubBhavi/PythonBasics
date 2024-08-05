# Exception: an exception is an event that occur during the execution of a program

a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
try:
    c = a / b
    print(c)
except Exception as error:
    print("A number is never divisible by 0")

