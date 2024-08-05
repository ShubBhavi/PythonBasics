number=(1,2,3,4,6,7)

def square(x):
    return x**2


print(sorted(list(map(square,number))))

print(tuple(map(str,number)))


#taking 5 numbers from the input and printing them

number1=(list(map(int,input("enter the numebrs").split())))
print(number1)