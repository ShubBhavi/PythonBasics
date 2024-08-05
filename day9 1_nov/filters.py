# numbers=[1,2,3,4,5,6,7,8,9,10]
# 
# def even_num(num):
#     return num%2==0
# 
# even_number= filter(even_num,numbers)
# print(even_number)
# even_number_list=list(even_number)
# print(even_number_list)

# words=["apple","shubham","rahul","sanjana","disha","hansa"]
# min_len=6
#
# def check_len(word):
#     return len(word)>min_len
#
# len1=filter(check_len,words)
# print(len1)
# print("op=",list(len1))
#
number=[1,2,3,4,5,6]

# def ifnum():
#     if i in number:
#         print("its is present")
#     else:
#         print("its is not ")
#
# i=int(input("enter the value of i"))
# ifnum()


# def even(num):
#     return num%2==0
#
# even_num=filter(even,number)
# print(list(even_num))

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

# def name_len(name):
#     return len(name)>4
#
# new_names=filter(name_len,names)
# print(list(new_names))
name=[]
for i in names:
    if len(i)>3:
        name.append(i)
print(name)