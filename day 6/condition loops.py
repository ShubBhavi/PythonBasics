# age=float(input("enter the age "))
# if age>18 :
#     print("the age boy can watch a movie")
# elif age<18:
#     print("the age boy cannot watch the movie")
# else:
#     print("still needs time")
#
# Loops,range
#
# for x in range(0,10,2):
#    print(x)
#
# x=list(range(1,5))
# print(x)
#
# for i in range(1, 10):
#     print(i)
#
# while loop
# i=0
# while (i<5):
#     print("hello")
#     i=i+1
#
#
# Break
#
# age=int(input("enter the age of a person"))
# if age<10:
#     print("he is a child")
# elif age>18:
#     print("he is allowed in the pub")
# elif age>60:
#     print("he is senior citizen")


# hannu=[]
# fruits=("mango","apple","papaya","orange","pineapple")
# print(fruits)
# for x in fruits:
#     if len(x)<7:
#      hannu.append(x)
#     elif len(x)<5:
#         print(x)
# print(hannu)


num=int(input("enter the number"))

match num:
    case 1:
        print("the number is 1")
    case 2:
        print("num is two")
    case _:
        print("dont even know which number is this ")