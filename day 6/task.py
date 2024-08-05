number = int(input("entert the number"))
if number < 0:
    print("factorial is not possible")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
        print(fact)


def sqaure(x):
    return x**2
#
# def cube(y):
#     return y**3
#
# num=int(input("enter the value to be performed"))
# print("the square of number is ",sqaure(num))
numbers=[1,2,3,4,5,6]

print(list(map(sqaure,numbers)))


# year = int(input("enter the year"))
# if (year % 4 == 0) or  (year % 100 != 0) and (year % 400 == 0):
#     print("its a leap year")
# else:
#     print("not a leap year")
