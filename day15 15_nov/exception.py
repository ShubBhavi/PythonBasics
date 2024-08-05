try:
    num1=int(input("enter the num"))
    num2=int(input("enter the num"))
    result=num1/num2

except ValueError as e:
    print("wrong numbers")
except ZeroDivisionError as e:
    print("not divisible")
else:
    print(result)