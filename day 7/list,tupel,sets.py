# a={1,2,}
# b={2,1}
# print("d=",a+b)

# nested tuple
# print("d=",(a,b))

# sets{}
# union sets

# print("d=",a.union(b))

# print("d=",a.intersection(b))

# print("d=",a.difference(b))
# print("d=",b.difference(a))

# print("d=",a.issubset(b))

a={1,2,3,4,5}
b={1,2,3,4,5,6,7,8}
print(a)
print("c=",(a,b))
print("c=",a.union(b))
print("c=",a.intersection(b))
print("c=",a.issubset(b))
print("c=",b.difference(a))
print("c=",a.difference(b))
print("c=",a.difference(b))

d=[1,2,3,4,5,6,7]
d.insert(1,0)

list1 = [1, 2, 3]
list2 = list1
print(id(list2))
print(id(list1))
print(list1 is list2)





