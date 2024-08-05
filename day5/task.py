# radius = float(input(print("enter the value of r")))
# area = 3.143 * radius ** 2
# print("area", area)

# a=int(input("enter the number for a"))
# print(a)
# b=int(input("enter the number for b"))
# print(b)
# 
# result= a if a>b else b
# print("the greater nmber is: ",result)

num1=int(input("enter ua num1"))
num2=int(input("enter ua num2"))
num3=int(input("enter ua num3"))
max_num= num1 if \
    (num1>num2 and num1>num3)\
    else\
    (num2 if num2>num3 else num3)
print("max_num=",max_num)