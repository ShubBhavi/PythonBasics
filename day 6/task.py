number = int(input("entert the number"))
if number < 0:
    print("factorial is not possible")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
        print(fact)
