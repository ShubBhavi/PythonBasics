list=[22,33,44,44,55]
print(list)

set1=(set(list))
print(set1)

# def add(x,y):
#     result=x+y
#     return result
#
# op=add(10,20)
# print(op)

def is_even(x):
    if x%2==0:
        print("%s is a even number" %x )
    else:
        print("%s is a not even number", x)


is_even(10)

set={1,2,3,4,5}
print(set)