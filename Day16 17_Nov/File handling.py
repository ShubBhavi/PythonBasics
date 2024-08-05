#File handling
#how to read a text and write
#
with open("shubham",'r') as file:
    content=file.read()
    print(content)
#
# with open("rahul",'w') as file:
#     file.write("wasuupp shubham bhavi")

#read line, read a full line and it dosent read second line
with open("rahul",'r') as file:
    line=file.readline()
    print(line)

#this is read lines
with open("rahul",'r') as file:
    line1=file.readlines()
    # print(line1)
    # this read line but in list format
    for line in line1:
        print(line,end='')







#how to open a file
#sytax



#read a file
#write into a file

